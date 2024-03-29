from rest_framework import serializers
from adree.models import SignUp
import hashlib
from django.contrib.auth.hashers import make_password


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model=SignUp
        fields=['userid','name','birthdate','email','gender','city','password']
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(SignUpSerializer, self).create(validated_data)

   

