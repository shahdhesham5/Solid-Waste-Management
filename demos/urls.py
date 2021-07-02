from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from . import views

urlpatterns = [
    path('', login_required(TemplateView.as_view(template_name='demos/demos/idsc.html'))),

    path('/timeseriesview', TemplateView.as_view(template_name='demos/demos/timeseries.html')),
    path('/timeseries', views.Timeseries.as_view(), name='timeseries'),

    path('/idsc_admin', views.IDSCAdmin.as_view(), name='idsc_admin'),


    path('/update_geojson', views.GeoJSON.as_view(), name='GeoJSON'),
    path('/hospital', views.Hospital.as_view(), name='hospital'),
]
