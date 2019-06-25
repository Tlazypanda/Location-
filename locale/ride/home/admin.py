from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Ride)
admin.site.register(Vehicle)
admin.site.register(Source)
admin.site.register(Dest)
admin.site.register(SourceCity)
admin.site.register(DestCity)
