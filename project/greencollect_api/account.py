from django.shortcuts import render
from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class AccountCreationSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'password', 'email', 'first_name', 'last_name')

class AccountSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'email', 'first_name', 'last_name')

class AccountConnectionSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'password')
        
        def to_internal_value(self, data):   
            try:
                username = data["username"]
                user = User.objects.get(username=username)
            except KeyError:
                raise serializers.ValidationError({'username':'Please Input your username'})
            except ValueError:
                raise serializers.ValidationError({'username':'Username Not Valid'})
            except User.DoesNotExist:
                raise serializers.ValidationError({'username':'Username does not exists'})

            try:
                username = data["password"]
            except KeyError:
                raise serializers.ValidationError({'password':'Please Input your password'})
            return data


class AccountView(ModelViewSet):

    def create(self, request):
        '''
        Create a new user
        '''
        serialized = AccountCreationSerializer(data = request.data)

        if serialized.is_valid():
            user = User.objects.create_user(
                username = serialized.data['username'],
                password = serialized.data['password'],
                email = serialized.data['email'],
                first_name = serialized.data['first_name'],
                last_name = serialized.data['last_name'],
            )
            serializedResponse = AccountSerializer(instance = user)
            return Response(serializedResponse.data , status = status.HTTP_201_CREATED)
        
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path=r'login', url_name='login')
    def login(self, request):
        '''
        Allow to login the given user
        '''
        serialized = AccountConnectionSerializer(data = request.data)

        if serialized.is_valid():
            username = serialized.data['username']
            password = serialized.data['password']
            user = User.objects.get(username=username)
            if user.check_password(password):
                Token.objects.filter(user=user).delete()
                token = Token.objects.create(user=user).key
                return Response({"token": token}, status=status.HTTP_200_OK)

            else:
                return Response(serialized.errors, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        '''
        Allow to logout the given user
        '''
        username = request.data['username']
        user = User.objects.get(username=username)
        Token.objects.filter(user=user).delete()

        return Response({"res": "User [" + username + "] disconnected"},
            status=status.HTTP_200_OK)
