from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class PredResults(models.Model):
    auther=models.OneToOneField(User, on_delete=models.CASCADE, related_name='predict_predict')
    Test199=models.PositiveIntegerField(default=1,blank=True,null=True)
    Test220 = models.PositiveIntegerField(default=0,blank=True,null=True)
    Test215 = models.PositiveIntegerField(default=0,blank=True,null=True)
    Test14 = models.PositiveIntegerField(default=0,blank=True,null=True)
    Test20 = models.PositiveIntegerField(default=0,blank=True,null=True)
    Test22 = models.PositiveIntegerField(default=0,blank=True,null=True)
    Test55 = models.PositiveIntegerField(default=0,blank=True,null=True)
    Test1 = models.PositiveIntegerField(default=0,blank=True,null=True)
    Test54 =models.PositiveIntegerField(default=0,blank=True,null=True)
    Test57 = models.PositiveIntegerField(default=0,blank=True,null=True)
    Heart_Disease = models.CharField(max_length=30)

    def __str__(self):
        return self.Heart_Disease+self.auther.username

