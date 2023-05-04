from rest_framework import serializers
from user.models import UserProfile, Interest
from hometoofficelinevector.models import UserHomeOfficeGap
from django.contrib.auth.models import User
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class InterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    is_superuser = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(UserSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            # for multiple fields in a list
            for field_name in remove_fields:
                self.fields.pop(field_name)

    class Meta:
        model = User
        read_only_fields = ['id']
        exclude = ["password", "username",]


class UserProfileSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True)
    user = UserSerializer(remove_fields=[
                          'is_superuser', "last_login", "is_staff", "is_active", "date_joined", "groups", "user_permissions"])

    class Meta:
        model = UserProfile
        exclude = ("date_created", "date_modified",
                   "is_deleted")


class UserHomeOfficeGapSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = UserHomeOfficeGap
        geo_field = "home_off_gap"
        fields = '__all__'
