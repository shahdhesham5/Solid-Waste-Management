from django.urls import path
from . import views as geoleaflet



urlpatterns =[

path('',
    geoleaflet.leaflet_index,
    name='geoleaflet'),
path('/map',geoleaflet.leaflet_index_map,name='geoleaflet_map'),
path('/dashboard',geoleaflet.leaflet_index_dashboard,name='geoleaflet_dashboard'),
]
