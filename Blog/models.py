from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Account(models.Model):
    GENDER_CHOICES = (('آقا', 'آقا'), ('خانم', 'خانم'),)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='account')
    phone=models.CharField(max_length=11,null=True,blank=True)
    gender=models.CharField(max_length=5,choices=GENDER_CHOICES,default='خانم')
    address=models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    age=models.PositiveIntegerField(default=0,blank=True,null=True)

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name