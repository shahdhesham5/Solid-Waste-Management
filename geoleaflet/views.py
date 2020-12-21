from django.shortcuts import render

# Create your views here.

def leaflet_index(request):
    return render(request,'geoleaflet/index.html')



def leaflet_index_map(request):
    return render(request,'geoleaflet/map.html')


def leaflet_index_dashboard(request):
    return render(request,'geoleaflet/dashboard.html')
