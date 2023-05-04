from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from os.path import join


def get_upload_path(instance, filename):
    return join('user_document', instance.user.username, filename)


class Interest(models.Model):
    area_of_interest = models.CharField(
        max_length=55, verbose_name=_("Interest"))

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("Interests")
        
    def __str__(self) -> str:
        return self.area_of_interest


class UserProfile(models.Model):
    GENDER_CHOICES = [("Male", _("Male")), ("Female",
                                            _("Female")), ("Other", _("Other"))]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Profile', null=True,
                             blank=True)

    first_name = models.CharField(max_length=55, blank=False, null=False)
    middle_name = models.CharField(max_length=55, blank=True, null=True)
    last_name = models.CharField(max_length=55, blank=True, null=True)
    gender = models.CharField(max_length=15, default="Male",
                              choices=GENDER_CHOICES)
    country = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=64, blank=False, null=False)
    phone = models.CharField(max_length=64, blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    interests = models.ManyToManyField(to=Interest, related_name="user_interest", blank=True, null=True)
    document = models.FileField(upload_to=get_upload_path, null=True, blank=True)
    home_address = models.PointField(srid=4326, null=True, blank=True)
    office_address = models.PointField(srid=4326, null=True, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, verbose_name="Is User Deleted")
    objects = models.Manager()
    

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")

    def __str__(self):
        return str(self.user.username)
    

    


