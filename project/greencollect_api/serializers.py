from rest_framework import serializers
from .models import Preventive, Waste, CommunityCollect

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
