from django.urls import path
from . import views


urlpatterns = [
 path('', views.main, name='main'),
 path('mainLogin', views.login, name='mainLogin'),
 path('<int:pk>',views.country_projects,name='country_projects'),
 path('projects/<int:pk>',views.project_details,name='project_details'),
 path('mainLogout',views.mainLogout,name='mainLogout'),

 ]
