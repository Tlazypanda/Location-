from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta

TRAVELTYPE = (
    (1, "LONG DISTANCE"),
    (2, "POINT TO POINT"),
    (3, "HOURLY RENTAL"),
)

PACKAGE = (
    (1, "4HRS AND 40KMS"),
    (2, "8HRS AND 80KMS"),
    (3, "6HRS AND 60KMS"),
    (4, "10HRS AND 100KMS"),
    (5, "5HRS AND 50KMS"),
    (6, "3HRS AND 30KMS"),
    (7, "12HRS AND 120KMS"),
)

CARS = (
    (1,"MICRO"),
    (2,"MINI"),
    (3,"SEDAN"),
    (4,"SUV")
)

# Create your models here.

class CustomUser(AbstractUser):
    address = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    country_of_residence = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    photo_url = models.CharField(max_length=255, blank=True, null=True)
    removed = models.IntegerField(default=0)
    user_type = models.CharField(max_length=255, blank=True, null=True)
    allow_app_access = models.BooleanField(default=False, blank=False)

class Vehicle(models.Model):
    company = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(max_length=10, choices=CARS)

class Source(models.Model):
    from_lat = models.CharField(max_length=50, blank=True, null=True)
    from_long = models.CharField(max_length=50, blank=True, null=True)
    desc = models.CharField(max_length=50, blank=True, null=True)

class Dest(models.Model):
    to_lat = models.CharField(max_length=50, blank=True, null=True)
    to_long = models.CharField(max_length=50, blank=True, null=True)
    desc = models.CharField(max_length=50, blank=True, null=True)

class SourceCity(models.Model):
    city_name = models.CharField(max_length=50, blank=True, null=True)
    source= models.ForeignKey(Source, on_delete=models.CASCADE)

class DestCity(models.Model):
    city_name = models.CharField(max_length=50, blank=True, null=True)
    dest= models.ForeignKey(Dest, on_delete=models.CASCADE)


class Ride(models.Model):
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    package =  models.IntegerField(max_length=10, choices=PACKAGE)
    travel_type =  models.IntegerField(max_length=10, choices=TRAVELTYPE)
    booking_created = models.DateTimeField(auto_now_add=True)
    from_area = models.ForeignKey(Source, on_delete=models.CASCADE,blank=True , null=True)
    to_area = models.ForeignKey(Dest, on_delete=models.CASCADE,blank=True , null=True)
    from_city = models.ForeignKey(SourceCity, on_delete=models.CASCADE,blank=True , null=True)
    to_city = models.ForeignKey(DestCity, on_delete=models.CASCADE,blank=True , null=True)
    is_canceled = models.IntegerField(default=0)
    is_booked_mobile = models.IntegerField(default=0)
    from_time = models.DateTimeField(blank=True , null=True, default=datetime.now())
    to_time = models.DateTimeField(blank=True , null=True)
    is_completed = models.IntegerField(default=0)
