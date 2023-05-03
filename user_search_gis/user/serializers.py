from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password", "username"]
        extra_kwargs = {"email": {"write_only": True, "required": True},
                        "username": {"write_only": True, "required": True},
                        "password": {"write_only": True, "required": True},
                        "first_name": {"write_only": True, "required": True},
                        "last_name": {"write_only": True, "required": False},
                        "date_joined": {"write_only": True, "required": False},
                        }