from rest_framework import serializers
from user.models import UserProfile, Interest

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'
        
        
class UserProfileSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True)
    
    class Meta:
        model = UserProfile
        fields = '__all__'