from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from . forms import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from predict import models
import pandas as pd
# Create your views here.
def index(request):
    #return HttpResponse("به وبلاگ ما و خودتان خوش آمدید")
   return render(request,'blog/index.html')


def SignupView(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            HttpResponse('you are welcome')
            return render(request, 'blog/index.html')
    form=UserCreationForm()
    return render(request,'blog/accounts/signup.html',{'form':form})


def LoginView(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("Blog:index")
    form=AuthenticationForm()
    return render(request, 'blog/accounts/login.html', {'form': form})

def LogoutView(request):
    logout(request)
    return redirect("Blog:index")


def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('blog:index')
                else:
                    return HttpResponse('اکانت شما غیرفعال است')
            else:
                return HttpResponse('اطلاعات شما نادرست است')
    else:
        form=LoginForm()
        return render(request,'blog/forms/account/login.html')



@login_required(login_url="blog:index")
def change_password(request):
    if request.method == 'POST':
        user=request.user
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            old_password=cd['old_password']
            new_password1=cd['new_password1']
            new_password2=cd['new_password2']
            if not user.check_password(old_password):
                return HttpResponse("پسورد قبلی شما درست نیست")
            elif new_password1 != new_password2:
                return HttpResponse("پسوردهای جدید شما با هم مطابقت ندارد")
            else:
                user.set_password(new_password1)
                login(request, user)
                user.save()
                return redirect("blog:index")#return HttpResponse("پسورد شما تغییر کرد")
    else:
        form=ChangePasswordForm()
    return render(request,'blog/forms/account/change_password.html',{'form':form})


def ContactUs(request):
    sent=False
    if request.method=='POST':
        form=ContactusForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject=cd['subject']
            name=cd['name']
            email=cd['email']
            phone=cd['phone']
            message=cd['message']
            msg="name:{0}\nphone:{1}\nemail:{2}\nmessage:\n{3}".format(name,phone,email,message)
            send_mail(subject,msg,'zarefateme24270@gmail.com',['zarefateme24270@gmail.com'],fail_silently=False)
            sent=True
    else:
        form=ContactusForm()
    return render(request,'blog/forms/contact_us.html',{'form':form,'sent':sent})


@api_view(['GET'])
def getusers(request):
    user=User.objects.all()
    serializer=UserSerializer(user,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def signup(request):
    data=request.data
    user=User.objects.create(
        username=data['username'],
        password=data['password'],
        is_active=data['is_active'],
        is_superuser=data['is_superuser'],
        is_staff=data['is_staff'],
    )
    serializer=UserSerializer(user,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def vorod(request):
    user=request.user
    login(request,user)
    return Response('it is login')


@api_view(['PUT'])
def updateuser(request,pk):
    data=request.data
    user=User.objects.get(id=pk)
    serializer=UserSerializer(user,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def getpredict(request):
    pre=models.PredResults.objects.all()
    serializer=ShowPredictSerializer(pre,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createpredict(request):
    data=request.data
    print(request.user)
    user = request.user
    print("dataaaaaaaaaaa",data)
    model = pd.read_pickle(r"svmmodel.pickle")
    # Make prediction
    result = model.predict([[data['Test199'], data['Test220'], data['Test215'], data['Test14'], data['Test20'], data['Test22'],
                             data['Test55'], data['Test1'], data['Test54'], data['Test57']]])
    print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",result[0])


    pre=models.PredResults.objects.create(
        Test199=data['Test199'],
        Test220=data['Test220'],
        Test215=data['Test215'],
        Test14=data['Test14'],
        Test20=data['Test20'],
        Test22=data['Test22'],
        Test55=data['Test55'],
        Test1=data['Test1'],
        Test54=data['Test54'],
        Test57=data['Test57'],
        Heart_Disease=result[0],
        auther=user
    )


    serializer=PredictSerializer(pre,many=False)
    return Response('it is done')
