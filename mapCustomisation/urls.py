from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name='dd'),
    path("d",index2,name='ddd'),
    path("recieve",recieve,name='recieve'),
    path("Layers_Edited",Layers_Edited,name='Layers_Edited'),
    path("AcceptLayer",AcceptLayer,name='AcceptLayer'),
    path("RejectedEdits",RejectedEdits,name='RejectedEdits')

]
