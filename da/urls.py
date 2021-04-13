from django.urls import path
from . import views as dd

urlpatterns = [
    path("",dd.index,name='dd'),
    path("d",dd.index2,name='ddd'),
]
