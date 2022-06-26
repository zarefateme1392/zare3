from django.urls import path
from . import views
app_name='predict'
urlpatterns=[
    path('index/',views.index,name='index'),
    path('predict/',views.UserPredict,name='predict'),

]