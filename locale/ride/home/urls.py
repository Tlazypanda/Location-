from django.urls import include, path
from django.conf.urls import url, include
from .views import *

urlpatterns = [


    url(
    r'^add_ride/$',add_ride),
    url(
    r'^(?P<ride_id>\d+)/edit_ride/$',edit_ride),
    url(
    r'^(?P<ride_id>\d+)/complete_ride/$',complete_ride),
    url(
    r'^(?P<ride_id>\d+)/cancel_ride/$',cancel_ride),
    url(
    r'^get_rides/$',get_rides)

]
