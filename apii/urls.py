from django.urls import path
from . import views as apii



urlpatterns = [
## include your urls here
    path('',apii.show,name='show'),
    path("<int:pk>",apii.details,name='details'),
     path("delete/<int:pk>",apii.delete,name='delete'),
     path("update/<int:pk>",apii.update,name='update'),
     path('create',apii.create,name='add'),

]
