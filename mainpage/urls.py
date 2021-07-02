from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse ,reverse_lazy

urlpatterns = [
 path('', views.main, name='main'),
 path('mainLogin', views.login, name='mainLogin'),
 path('<int:pk>',views.country_projects,name='country_projects'),
 path('projects/<int:pk>',views.project_details,name='project_details'),
 path('mainLogout',views.mainLogout,name='mainLogout'),
 path('change-password/',
      auth_views.PasswordChangeView.as_view(
          template_name='main/change-password.html',
           success_url = reverse_lazy('main'),
            ),
      name='change-password'),
  path('password_change/',views.password_change,name='password_change'),

 ]
