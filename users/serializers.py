from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    cash = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ['id', 'username','cash', 'image' ,'email', 'is_active', 'date_joined']