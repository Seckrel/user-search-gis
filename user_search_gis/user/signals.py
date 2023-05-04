from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        defaults = {
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "email": instance.email,
            "home_address": Point(0.0, 0.0),
            "office_address": Point(0.0, 0.0)
        }
        try:
            userprofile, _ = UserProfile.objects.update_or_create(user = instance, defaults=defaults)
        except Exception as e:
            print(e)
        
    

    