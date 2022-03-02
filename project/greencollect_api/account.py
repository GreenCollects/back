from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import serializers

class AccountCreationSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'password', 'email', 'first_name', 'last_name')

class AccountSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'email', 'first_name', 'last_name')

class AccountView(APIView):

    def post(self, request):
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
