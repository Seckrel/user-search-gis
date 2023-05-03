from django.db.models.signals import pre_save
from django.dispatch import receiver
from user.models import UserProfile
from .models import UserHomeOfficeGap
from django.contrib.gis.geos import LineString




@receiver(pre_save, sender=UserProfile)
def update_home_to_office_point(sender, instance, **kwargs):
    home_address = instance.home_address
    office_address = instance.office_address
    gap_line = LineString(home_address, office_address)
    
    UserHomeOfficeGap.objects.update_or_create(user=instance, defaults={'home_off_gap': gap_line})
    

    