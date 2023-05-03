from django.contrib import admin
from .models import UserProfile, Interest
from leaflet.admin import LeafletGeoAdmin


@admin.register(UserProfile)
class CustomUserAdmin(LeafletGeoAdmin):
    pass

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    pass


