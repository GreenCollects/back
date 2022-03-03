from rest_framework import serializers
from .models import Participation, Point, Preventive, Waste, CommunityCollect, Rating

class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = '__all__'
    
class CommunityCollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityCollect
        fields = '__all__'

class PreventiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preventive
        fields = '__all__'

class PointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = '__all__'