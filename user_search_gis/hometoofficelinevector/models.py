from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _    
from user.models import UserProfile


class UserHomeOfficeGap(models.Model):
    user = models.OneToOneField(to=UserProfile, on_delete=models.CASCADE, related_name="user_userhomeoffice")
    home_off_gap = models.LineStringField(verbose_name="Line Vector from home to office", null=True, blank=True)
    
    class Meta:
        verbose_name = _("User Home Office Gap")
        verbose_name_plural = _("Users Home Office Gap")
        
    def __str__(self):
        return str(self.user.user.username)