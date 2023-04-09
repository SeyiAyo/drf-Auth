from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, fields, viewsets
from rest_framework import status
from rest_framework.decorators import api_view



# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

#Class based view to register user
#class RegisterUserAPIView(generics.CreateAPIView):
class RegisterUserAPIView(viewsets.ModelViewSet):


  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer 
  
  def create(self, request, *args, **kwargs):
    queryset = User.objects.all()
    serializer = self.get_serializer(data=request.data)
    self.perform_create(serializer)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)