from rest_framework import serializers

from locations.models import Location, User

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields='__all__'

class UserLocationSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'