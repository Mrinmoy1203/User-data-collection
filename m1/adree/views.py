
# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import SignUp as SignUpModel
from .serializers import SignUpSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.
class SignUp(generics.ListCreateAPIView,generics.DestroyAPIView):
    queryset = SignUpModel.objects.all()
    serializer_class = SignUpSerializer
    

class SingleUserView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = SignUpModel.objects.all()
    serializer_class = SignUpSerializer

  #def hash(queryset):
    # hashlib.md5(SignUpModel.objects.password())
