from django.apps import AppConfig
from django.core.signals import setting_changed


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self) -> None:
        from hometoofficelinevector.signals import update_home_to_office_point
        from .signals import create_user_profile
        from django.contrib.auth.models import User
        from .models import UserProfile

        setting_changed.connect(update_home_to_office_point, sender=UserProfile)
        setting_changed.connect(create_user_profile, sender=User)