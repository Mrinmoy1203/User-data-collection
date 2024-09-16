
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
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login as auth_login
from .serializers import LoginSerializer

# Create your views here.
class SignUp(generics.ListCreateAPIView,generics.DestroyAPIView):
    queryset = SignUpModel.objects.all()
    serializer_class = SignUpSerializer
    

class SingleUserView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = SignUpModel.objects.all()
    serializer_class = SignUpSerializer

  #def hash(queryset):
    # hashlib.md5(SignUpModel.objects.password())
# views.py
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)  # Logs the user in
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

