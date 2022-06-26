from django import forms
import numpy as np
from .models import *
class PredictForm(forms.Form):
    name = forms.CharField(required=True,label='name')
    last_name = forms.CharField(required=True,label='last_name')
    Test199 = forms.IntegerField(required=True,label='Test199')
    Test220 = forms.IntegerField(required=True,label='Test220')
    Test215 = forms.IntegerField(required=True,label='Test215')
    Test14 = forms.IntegerField(required=True,label='Test14')
    Test20 = forms.IntegerField(required=True,label='Test20')
    Test22 = forms.IntegerField(required=True,label='Test22')
    Test55 = forms.IntegerField(required=True,label='Test55')
    Test1 = forms.IntegerField(required=True,label='Test1')
    Test54 = forms.IntegerField(required=True,label='Test54')
    Test57 = forms.IntegerField(required=True,label='Test57')
