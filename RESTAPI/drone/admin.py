from django.contrib import admin
from .models import Drone, Competition, DroneCategory, Pilot
# Register your models here.

admin.site.register(Drone)
admin.site.register(Competition)
admin.site.register(DroneCategory)
admin.site.register(Pilot)
