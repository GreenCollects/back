from rest_framework import serializers
from .models import Point, Preventive, Waste, CommunityCollect, Rating

class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = ["label", "creationDate", "updateDate"]
    
class CommunityCollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityCollect
        fields = '__all__'

class PreventiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preventive
        fields = '__all__'

class PointSerializer(serializers.ModelSerializer):
    # collect = serializers.PrimaryKeyRelatedField(queryset =Waste.objects.all(), many=True)

    class Meta:
        model = Point
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'