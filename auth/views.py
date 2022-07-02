from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework import generics

'''
    Login and Register User — Django Rest Framework
    https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5 
'''
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,) # What does the ',' do here ?
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer