
from geopy import distance
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import permissions, status
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .decorators import permission_method
from .models import (CommunityCollect, Participation, Point, Preventive,
                     Rating, Waste)
from .serializers import (CommunityCollectSerializer, ParticipationSerializer,
                          PointSerializer, PreventiveSerializer,
                          RatingSerializer, WasteSerializer)


# Create your views here.

#View for waste (batteries,Huiles,....)
class WasteView(APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    @permission_method((AllowAny,))
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

#View for Community collect
class CommunityCollectView(APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        communityCollects = CommunityCollect.objects.all()
        serializer = CommunityCollectSerializer(communityCollects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommunityCollectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#View for a single community collect
class CommunityCollectDetailsView(APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return CommunityCollect.objects.get(id=id)

        except CommunityCollect.DoesNotExist:
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        communityCollect = self.get_object(id)
        serializer = CommunityCollectSerializer(communityCollect)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        communityCollect = self.get_object(id)
        serializer = CommunityCollectSerializer(
            communityCollect, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        communityCollect = self.get_object(id)
        communityCollect.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#View for preventive ads and virtuous products
class PreventiveView(APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        preventive = Preventive.objects.all()
        serializer = PreventiveSerializer(preventive, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PreventiveSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#View for a single preventive ads and virtuous products
class PreventiveDetailsView(APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return Preventive.objects.get(id=id)

        except Preventive.DoesNotExist:
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        preventive = self.get_object(id)
        serializer = PreventiveSerializer(preventive)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        preventive = self.get_object(id)
        serializer = PreventiveSerializer(preventive, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        preventive = self.get_object(id)
        preventive.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#View for a collect point
class PointView (APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        points = Point.objects.all()
        serializer = PointSerializer(points, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PointSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#View for a single collect point
class PointDetailsView (APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return Point.objects.get(id=id)

        except Point.DoesNotExist:
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        points = self.get_object(id)
        serializer = PointSerializer(points)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        point = self.get_object(id)
        serializer = PointSerializer(point, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        point = self.get_object(id)
        point.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#View for a collect comunity and collect point into a circle with a certain radius
class PointAreaView(APIView):
    
    def post(self,request):
        points = Point.objects.all()
        collects = CommunityCollect.objects.all()
        point_serializer = PointSerializer(points, many=True)
        collect_serializer = CommunityCollectSerializer(collects, many=True)
        point_data = point_serializer.data
        collect_data = collect_serializer.data
        circleLatitude = request.data.get('latitude')
        circleLongitude = request.data.get('longitude')
        radius = request.data.get('radius')
        data = point_data + collect_data
        response= []
        if (circleLatitude is not None) and (circleLongitude is not None) and (radius is not None):
            circleCoordinate = (circleLatitude, circleLongitude)
            for marker in data :
                markercoordinate = (marker.get('latitude'), marker.get('longitude'))
                if (distance.distance(markercoordinate, circleCoordinate).km < radius) :
                    response.append(marker)
            
            return Response(response, status=status.HTTP_200_OK)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)


#View for points rates
class RatingView (APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        marks = Rating.objects.all()
        serializer = RatingSerializer(marks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RatingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#View for a single point rates
class RatingDetailsView (APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return Rating.objects.get(id=id)

        except Rating.DoesNotExist:
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        mark = self.get_object(id)
        serializer = RatingSerializer(mark)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        mark = self.get_object(id)
        serializer = RatingSerializer(mark, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        mark = self.get_object(id)
        mark.delete()
        return Response(status=status.HTTP_200_OK)

class RatingValueView (APIView):
    def get(self, request, idPoint):
        point = Point.objects.get(pk=idPoint)
        rate = Rating.objects.filter(point=point).aggregate(avg=Avg('rate'))["avg"]
        
        return Response({"idPoint": idPoint , "rate": rate, "denominator": 10}, status=status.HTTP_200_OK)

class RatingUserPointView (APIView):
    def get(self, request, idPoint):
        point = Point.objects.get(pk=idPoint)
        try:
            rate = Rating.objects.get(point=point, user=request.user)
            serializer = RatingSerializer(rate)
        except Rating.DoesNotExist:
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data, status=status.HTTP_200_OK)

#View for participation list to a comunity collect
class ParticipationView(APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        participations = Participation.objects.all()
        serializer = ParticipationSerializer(participations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ParticipationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#View for a participation to a comunity collect
class ParticipationDetailsView(APIView):
    # TODO add permission to check if user is authenticated
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return Participation.objects.get(id=id)

        except Participation.DoesNotExist:
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        participation = self.get_object(id)
        serializer = ParticipationSerializer(participation)
        return Response(serializer.data)

    def put(self, request, id):
        participation = self.get_object(id)
        serializer = ParticipationSerializer(
            participation, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        participation = self.get_object(id)
        participation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
