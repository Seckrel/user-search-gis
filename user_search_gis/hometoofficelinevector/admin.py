from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import UserHomeOfficeGap

@admin.register(UserHomeOfficeGap)
class UserHomeOfficeGapAdmin(LeafletGeoAdmin):
    pass


