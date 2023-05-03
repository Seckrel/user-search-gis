from rest_framework.views import APIView, Response
from rest_framework.viewsets import GenericViewSet
from .serializers import UserSerializer
from .models import UserProfile
from rest_framework import status
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.mixins import CreateModelMixin


class RegisterUser(GenericViewSet, CreateModelMixin):
    serializer_class = UserSerializer
    
    def create(self, request):
        try:
            email = UserProfile.objects.filter(user__email=request.data.get("email"))
            if email.exists():
                return Response({"message": "Email is already registered"}, status=400)
            
            user = UserProfile.objects.filter(user__username=request.data.get("username"))
            if user.exists():
                return Response({"message": "Username is already taken"}, status=400)
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = serializer.save(is_active=False)
                user.set_password = serializer.validated_data["password"]
                user.save()
                return Response({"message": "User Created Successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": str(serializer.errors)}, status=400)
        
        except Exception as e:
            return Response({"message": str(e)}, status=400)
        
        
class UserSignIn(APIView):
    def post(self, request):
       username = request.data.get("username") 
       password = request.data.get("password")
       
       user = User.objects.filter(Q(username=username) | Q(password=password))
       if not user.exists():
           return Response({"message": "User does not exist"}, status=400)
       
       user = user[0]
       if user.check_password(password):
           return Response({"message": "User and Password does not match"}, status=403)
       
       if not user.is_active:
           return Response({"message": "Unverified account. Check your email to verify this account"}, status=400)
       
       token, created = Token.object.get_or_create(user=user)
       return Response({
           "token": token.key,
           'user_id': user.pk,
            'email': user.email,
            'username': user.username
       })
           
       
       
        
        