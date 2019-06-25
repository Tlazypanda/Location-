from django.shortcuts import render
from .models import *
from datetime import datetime, timedelta
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import  api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication

# Create your views here.

def response_500(log_msg, e):
    return Response({'status': 'error','message': 'Something went wrong.'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)


def response_400(message, log_msg, e):
    return Response({'status': 'error','message': message}, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_ride(request):

    user=request.user
    from_time= None
    if request.data['vehicle_id'] is None or request.data['vehicle_id'] is "":
        return response_400("Vehicle cant be blank","Vehicle cant be blank",None)
    vehicle_id = request.data['vehicle_id']
    if request.data['package_id'] is None or request.data['package_id'] is "":
        return response_400("package cant be blank","Package cant be blank",None)
    package = request.data['package_id']
    if request.data['travel_type'] is None or request.data['travel_type'] is "":
        return response_400("Traveltype cant be blank","Traveltype cant be blank",None)
    travel_type = request.data['travel_type']
    if request.data['source_id'] is None or request.data['source_id'] is "":
        return response_400("Source cant be blank","Source cant be blank",None)
    source_id = request.data['source_id']
    if request.data['dest_id'] is None or request.data['dest_id'] is "":
        return response_400("Destination cant be blank","Destination cant be blank",None)
    dest_id = request.data['dest_id']
    if 'from_time' in request.data:
        from_time = request.data['from_time']

    ride = Ride()
    ride.user = user
    ride.travel_type = travel_type
    ride.package = package
    if not(Vehicle.objects.filter(id = vehicle_id).exists()):
        return response_400("Vehicle doesn't exist","Vehicle doesn't exist",None)
    ride.vehicle = Vehicle.objects.get(id = vehicle_id)
    if travel_type==2:
        if not(Source.objects.filter(id = source_id).exists()):
            return response_400("Source doesn't exist","Source doesn't exist",None)
        ride.from_area = Source.objects.get(id = source_id)
        if not(Dest.objects.filter(id = dest_id).exists()):
            return response_400("Destination doesn't exist","Destination doesn't exist",None)
        ride.to_area = Dest.objects.get(id = dest_id)

    else:
        if not(SourceCity.objects.filter(id = source_id).exists()):
            return response_400("Source city doesn't exist","Source doesn't exist",None)
        ride.from_city = SourceCity.objects.get(id = source_id)
        if not(DestCity.objects.filter(id = dest_id).exists()):
            return response_400("Destination city doesn't exist","Destination doesn't exist",None)
        ride.to_city = DestCity.objects.get(id = dest_id)
    if from_time is not None or from_time is not "":
        ride.from_time = from_time

    ride.save()
    return Response(RideSerializer(ride).data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def edit_ride(request,ride_id):
    try:
        vehicle_id = None
        package_id = None
        travel_type = None
        source_id = None
        dest_id = None
        from_time = None
        if 'vehicle_id' in request.data:
            if request.data['vehicle_id'] is None or request.data['vehicle_id'] is "":
                return response_400("Vehicle cant be blank","Vehicle cant be blank",None)
            vehicle_id = request.data['vehicle_id']
        if 'package_id' in request.data:
            if request.data['package_id'] is None or request.data['package_id'] is "":
                return response_400("package cant be blank","Package cant be blank",None)
            package = request.data['package_id']
        if 'travel_type' in request.data:
            if request.data['travel_type'] is None or request.data['travel_type'] is "":
                return response_400("Traveltype cant be blank","Traveltype cant be blank",None)
            travel_type = request.data['travel_type']
        if 'source_id' in request.data:
            if request.data['source_id'] is None or request.data['source_id'] is "":
                return response_400("Source cant be blank","Source cant be blank",None)
            source_id = request.data['source_id']
        if 'dest_id' in request.data:
            if request.data['dest_id'] is None or request.data['dest_id'] is "":
                return response_400("Destination cant be blank","Destination cant be blank",None)
            dest_id = request.data['dest_id']
        if 'from_time' in request.data:
            from_time = request.data['from_time']

        if not(Ride.objects.filter(id = ride_id).exists()):
            return response_400("Ride doesn't exist","Ride doesn't exist",None)
        ride = Ride.objects.get(id = ride_id)
        if ride.is_completed == 1:
            return response_400("Ride is already completed","Ride is already completed",None)
        ride.travel_type = travel_type
        ride.package = package
        if not(Vehicle.objects.filter(id = vehicle_id).exists()):
            return response_400("Vehicle doesn't exist","Vehicle doesn't exist",None)
        ride.vehicle = Vehicle.objects.get(id = vehicle_id)
        if travel_type==2:
            if not(Source.objects.filter(id = source_id).exists()):
                return response_400("Source doesn't exist","Source doesn't exist",None)
            ride.from_area = Source.objects.get(id = source_id)
            if not(Dest.objects.filter(id = dest_id).exists()):
                return response_400("Destination doesn't exist","Destination doesn't exist",None)
            ride.to_area = Dest.objects.get(id = dest_id)

        else:
            if not(SourceCity.objects.filter(id = source_id).exists()):
                return response_400("Source doesn't exist","Source doesn't exist",None)
            ride.from_city = SourceCity.objects.get(id = source_id)
            if not(DestCity.objects.filter(id = dest_id).exists()):
                return response_400("Destination doesn't exist","Destination doesn't exist",None)
            ride.to_city = DestCity.objects.get(id = dest_id)
        if from_time is not None or from_time is not "":
            ride.from_time = from_time

        ride.save()
        return Response(RideSerializer(ride).data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message":"An error occured while booking."})


@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def cancel_ride(request, ride_id):
    try:
        if not(Ride.objects.filter(id = ride_id).exists()):
            return response_400("Ride doesn't exist","Ride doesn't exist",None)
        ride = Ride.objects.get(id = ride_id)
        if ride.is_completed==1:
            return response_400("Ride has already been completed","Ride has already been canceled",None)
        ride.is_canceled = 1
        ride.save()
        return Response(RideSerializer(ride).data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message":"An error occured while booking."})

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def complete_ride(request, ride_id):

    if not(Ride.objects.filter(id = ride_id).exists()):
        return response_400("Ride doesn't exist","Ride doesn't exist",None)
    ride = Ride.objects.get(id = ride_id)
    if ride.is_canceled==1:
        return response_400("Ride has already been canceled","Ride has already been canceled",None)
    ride.is_completed = 1
    ride.to_time = datetime.now()
    ride.save()
    return Response(RideSerializer(ride).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_rides(request):

        user = request.user
        queryset = Ride.objects.filter(user = user)
        if request.GET.get('package') is not None:
            package = request.GET.get('package')
            queryset = queryset.filter(package = package)
        if request.GET.get('travel_type') is not None:
            travel_type = request.GET.get('travel_type')
            queryset = queryset.filter(travel_type = travel_type)
        if request.GET.get('source_city') is not None:
            source_city = request.GET.get('source_city')
            city = SourceCity.objects.get(city_name = source_city)
            queryset = queryset.filter(from_city = city)
        if request.GET.get('dest_city') is not None:
            dest_city = request.GET.get('dest_city')
            city = DestCity.objects.get(city_name = dest_city)
            queryset = queryset.filter(to_city = city)

        return Response(RideSerializer(queryset,many=True).data, status=status.HTTP_201_CREATED)
