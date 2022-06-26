from django.contrib import admin
from .models import *
@admin.register(PredResults)
class PredResultsAdmin(admin.ModelAdmin):
    list_display=('auther','Test199','Test220','Test215','Test14','Test20','Test22','Test55','Test1','Test54','Test57','Heart_Disease',)
