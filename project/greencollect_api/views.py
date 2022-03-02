from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Waste, CommunityCollect, Preventive, Point, Rating
from .serializers import WasteSerializer, CommunityCollectSerializer, PreventiveSerializer, PointSerializer, RatingSerializer

# Create your views here.


class WasteView(APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the waste items
        '''
        wastes = Waste.objects.all()
        serializer = WasteSerializer(wastes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'label': request.data.get('label')
        }
        serializer = WasteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        '''
        Delete the given Waste
        '''
        waste = Waste.objects.get(label=request.data.get('label'))

        if not waste:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        waste.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class CommunityCollectView(APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        communityCollects = CommunityCollect.objects.all()
        serializer = CommunityCollectSerializer(communityCollects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommunityCollectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommunityCollectDetailsView(APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return CommunityCollect.objects.get(id=id)

        except CommunityCollect.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        communityCollect = self.get_object(id)
        serializer = CommunityCollectSerializer(communityCollect)
        return Response(serializer.data)

    def put(self, request, id):
        communityCollect = self.get_object(id)
        serializer = CommunityCollectSerializer(
            communityCollect, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        communityCollect = self.get_object(id)
        communityCollect.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PreventiveView(APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        preventive = Preventive.objects.all()
        serializer = PreventiveSerializer(preventive, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PreventiveSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PreventiveDetailsView(APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return Preventive.objects.get(id=id)

        except Preventive.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        preventive = self.get_object(id)
        serializer = PreventiveSerializer(preventive)
        return Response(serializer.data)

    def put(self, request, id):
        preventive = self.get_object(id)
        serializer = PreventiveSerializer(preventive, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        preventive = self.get_object(id)
        preventive.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PointView (APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request) :
        points = Point.objects.all()
        serializer = PointSerializer(points, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PointSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class PointDetailsView (APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]


    def get_object(self, id):
        try:
            return Point.objects.get(id=id)

        except Point.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id) :
        points = self.get_object(id)
        serializer = PointSerializer(points)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        point = self.get_object(id)
        serializer = PointSerializer(point, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        point = self.get_object(id)
        point.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class RatingView (APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request) :
        marks = Rating.objects.all()
        serializer = RatingSerializer(marks, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RatingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RatingDetailsView (APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]


    def get_object(self, id):
        try:
            return Rating.objects.get(id=id)

        except Rating.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id) :
        mark = self.get_object(id)
        serializer = RatingSerializer(mark)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        mark = self.get_object(id)
        serializer = RatingSerializer(mark, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        mark = self.get_object(id)
        mark.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
