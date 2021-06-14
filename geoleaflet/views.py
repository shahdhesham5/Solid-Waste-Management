from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# import leafmap

import json
# Create your views here.

def leaflet_index(request):
    return render(request,'geoleaflet/index.html')



def leaflet_index_map(request):
    return render(request,'geoleaflet/map.html')


def leaflet_index_dashboard(request):
    return render(request,'geoleaflet/dashboard.html')


def addg(request):
    points=AddG.objects.all()
    context={
        'points':points
    }
    return render (request,'geoleaflet/addg.html',context)
