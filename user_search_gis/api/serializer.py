from rest_framework import serializers
from user.models import UserProfile, Interest
from django.contrib.auth.models import User

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ["password", "username"]
        
        
class UserProfileSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True)
    
    class Meta:
        model = UserProfile
        fields = '__all__'