from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from . forms import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import pandas as pd
# Create your views here.
def index(request):
    #return HttpResponse("به وبلاگ ما و خودتان خوش آمدید")
   return HttpResponse('به app predict خوش آمدید')



def UserPredict(request):
    print(request.user)
    user=request.user
    try:
        account=PredResults.objects.get(auther=user)
    except:
        account=PredResults.objects.create(auther=user)
    if request.method=="POST":
        form=PredictForm(request.POST)
        print(form)
        if form.is_valid():
            print("yesgggggggggggggggggg")
            user.first_name=form.cleaned_data['name']
            print(user.first_name)
            user.last_name=form.cleaned_data['last_name']
            account.Test199=form.cleaned_data['Test199']
            account.Test220 = form.cleaned_data['Test220']
            account.Test215 = form.cleaned_data['Test215']
            account.Test14 = form.cleaned_data['Test14']
            account.Test20 = form.cleaned_data['Test20']
            account.Test22 = form.cleaned_data['Test22']
            account.Test55 = form.cleaned_data['Test55']
            account.Test1 = form.cleaned_data['Test1']
            account.Test54 = form.cleaned_data['Test54']
            account.Test57 = form.cleaned_data['Test57']
            print(account.Test57)
            model = pd.read_pickle(r"svmmodel.pickle")
            # Make prediction
            result = model.predict(
                [[account.Test199, account.Test220, account.Test215, account.Test14, account.Test20,account.Test22,account.Test55,account.Test1,account.Test54,account.Test57]])

            account.Heart_Disease = result[0]


            user.save()
            account.save()
            #return redirect('predict:index')
            return HttpResponse(result)
        return render(request,'forms/predict.html',{'form':form,'account':account})
    form=PredictForm()
    return render(request,'forms/predict.html',{'form':form,'account':account})
