from rest_framework import serializers


class PreferenceSerializer(serializers.Serializer):
    preference_type = serializers.CharField()