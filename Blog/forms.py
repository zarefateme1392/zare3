from django import forms
import numpy as np
from .models import *
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class ChangePasswordForm(forms.Form):
    old_password=forms.CharField(widget=forms.PasswordInput(),label='پسورد قبلی')
    new_password1 = forms.CharField(widget=forms.PasswordInput(), label='پسورد جدید')
    new_password2 = forms.CharField(widget=forms.PasswordInput(), label=' تکرار پسورد جدید')

    def clean_new_password1(self):
        password=self.cleaned_data.get("new_password1")
        print(len(password))
        if len(password)<8:
            raise forms.ValidationError("پسورد نباید کمتر از 8 کرکتر باشد")
        return password

    def clean_new_password2(self):
        password1=self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 != password2:
            raise forms.ValidationError("پسورد مطابقت ندارد")
        return password2

class ContactusForm(forms.Form):
    message=forms.CharField(widget=forms.Textarea,required=True,label='پیام')
    name=forms.CharField(max_length=25,required=True,label='نام')
    email=forms.EmailField(required=True,label='ایمیل')
    subject=forms.CharField(max_length=25,required=True,label='موضوع')
    phone=forms.CharField(max_length=11,required=False,label='تلفن')