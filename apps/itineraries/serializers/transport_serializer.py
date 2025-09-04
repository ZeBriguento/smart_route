from rest_framework import serializers
from apps.itineraries.models import Transport

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ["id", "name"]