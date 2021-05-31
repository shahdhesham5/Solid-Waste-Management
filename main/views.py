from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate ,login as auth_login
from django.contrib import messages

from django.urls import reverse ,reverse_lazy
import json
User = get_user_model()

# Create your views here.
def main(request):
    if request.user.is_authenticated :
        return render(request,'main/main.html')
    else:
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

        else:
            print('kkkkkkkkk')
            messages.error(request,'username or password not correct')
            return HttpResponseRedirect(reverse_lazy('main'))


    return HttpResponse('h')
    pass
