from rest_framework import serializers
from . models import Customer
from . models import Login

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login
        fields= ('Username','password')

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields= ('UserId','Id','title','body')

