from django.shortcuts import render
from django.http import HttpResponse
# import leafmap

import leafmap.foliumap as leafmaph
import json
# Create your views here.

def leaflet_index(request):
    return render(request,'geoleaflet/index.html')



def leaflet_index_map(request):
    return render(request,'geoleaflet/map.html')


def leaflet_index_dashboard(request):
    return render(request,'geoleaflet/dashboard.html')




def leafmap(request):
    print(leafmap)
    m = leafmaph.Map(center=(40, -100), zoom=4)
    # n= json.dumps(m.__dict__)
    print(type(m))
    context={
        'm':m
    }
    return HttpResponse(m)
    return render(request,'geoleaflet/leafmap.html')
