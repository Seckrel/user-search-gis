from django.urls import path
from .viewset import UserSignIn, RegisterUser

urlpatterns = [
    path('sign-in/', UserSignIn.as_view(), name='userlogin'),
    path('register-user/', RegisterUser.as_view({"post": "create"}), name='registeruser')
]