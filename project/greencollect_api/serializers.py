from rest_framework import serializers
from .models import Waste

class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = ["label", "creationDate", "updateDate"]