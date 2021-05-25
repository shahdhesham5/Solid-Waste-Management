from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate ,login as auth_login
from django.urls import reverse
import json
User = get_user_model()

# Create your views here.
def main(request):
    print('entered')
    if(request.user.username ):
        print(request.user)

        return render(request,'main/main.html')
    else:
        print(request.user)
        return render(request,'main/login.html')
        return HttpResponse('login')


def login(request):
    if request.method=='POST':
        userName=request.POST['userName']
        password=request.POST['password']
        user = authenticate(username=userName, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('main'))
        context={
            'message':"user or passwd is wrong"
        }
        return   render(request,'main/login.html',context)


    return HttpResponse('h')
    pass
