from rest_framework import serializers


class ActivitySerializer(serializers.Serializer):
    name = serializers.CharField()


class SpotSerializer(serializers.Serializer):
    name = serializers.CharField()
    activities = serializers.ListField(child=serializers.CharField())


class ProvinceSerializer(serializers.Serializer):
    province = serializers.CharField()
    spots = SpotSerializer(many=True)


class ItinerarySerializer(serializers.Serializer):
    itinerary = ProvinceSerializer(many=True)
    total_co2 = serializers.FloatField(allow_null=True)
    budget = serializers.FloatField()
    days = serializers.IntegerField()
    transport_type = serializers.CharField()
    preferences = serializers.ListField(child=serializers.CharField())
    suggestions = serializers.ListField(child=serializers.CharField())
