from django.urls import path
from . import views
app_name='Blog'
urlpatterns=[
    path('index/',views.index,name='index'),
    path('signup/',views.SignupView,name='signup'),
    #path('login/',views.LoginView,name='login'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.LogoutView,name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('contact-us/',views.ContactUs,name='contact_us'),
    path('alluser/',views.getusers,name='getusers'),
    path('allpredict/',views.getpredict,name='allpredict'),
    path('signup-user/',views.signup,name='signup-user'),
    path('update-user/<str:pk>/',views.updateuser,name='update-user'),
    path('createpredict/',views.createpredict,name='createpredict'),
    path('vorod/',views.vorod,name='vorod'),
]