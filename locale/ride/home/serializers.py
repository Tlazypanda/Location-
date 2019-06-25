from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'

class DestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dest
        fields = '__all__'

class SourceCitySerializer(serializers.ModelSerializer):
    source = SourceSerializer(read_only=True)
    class Meta:
        model = SourceCity
        fields = '__all__'

class DestCitySerializer(serializers.ModelSerializer):
    dest = DestSerializer(read_only=True)
    class Meta:
        model = DestCity
        fields = '__all__'

class RideSerializer(serializers.ModelSerializer):
    user = UserSerializer( read_only=True)
    vehicle = VehicleSerializer( read_only=True)
    from_area = SourceSerializer(read_only=True)
    to_area = DestSerializer(read_only=True)
    from_city = SourceCitySerializer(read_only=True)
    to_city = DestCitySerializer(read_only=True)

    class Meta:
        model = Ride
        fields = ('id','user','vehicle', 'travel_type', 'package', 'booking_created' ,'from_area','to_area','from_city','to_city','is_canceled','is_booked_mobile','from_time','to_time','is_completed')
