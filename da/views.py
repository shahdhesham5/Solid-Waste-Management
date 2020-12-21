from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
def index(request):
    d =Higis.objects.all()
    if 1  :
        return HttpResponse("kkkkkkkkkkkkkkkT")
    else:
        return HtttpResponse("n")
