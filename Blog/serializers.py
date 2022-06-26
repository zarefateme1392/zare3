

from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from predict import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("id","username","password","is_active","is_superuser","is_staff",)
class PredictSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.PredResults
        fields=(
            "Test199",
            "Test220",
            "Test215",
            "Test14",
            "Test20",
            "Test22",
            "Test55",
            "Test1",
            "Test54",
            "Test57",

                )
class ShowPredictSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.PredResults
        fields='__all__'