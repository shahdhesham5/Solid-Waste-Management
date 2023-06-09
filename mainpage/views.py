from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth import (authenticate ,
                                 login as auth_login,
                                 logout )
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from django.urls import reverse ,reverse_lazy
import json
User = get_user_model()
from .models import  (Group_Team,
                     Project_Country,
                     Project,
                     Project_task)



# List  the countries that has projects
def main(request):
    if request.user.is_authenticated :
        try:
            user_groups=request.user.groups.exclude(project_group=None)
            for user_group in user_groups:
                countries=user_group.project_group.project_countries.all()
            context={
                    'countries':countries
                    }
        except:
            context={
                'countries':[]
                    }
        return render(request,'main/countries.html',context)
    else:
        return render(request,'main/login.html')

# list the projects in each country
def country_projects(request,pk):
    country=Project_Country.objects.get(id=pk)
    # list user groups
    user_groups=request.user.groups.exclude(project_group=None)
    # query to filter if the project group in project groups
    projects=country.projects.filter(project_group__in=
                                map(lambda x:x.project_group,user_groups))
    context={
        'projects':projects,
        'country':country
    }
    return render(request,'main/country_projects.html',context)

# show the details of the project like intro
def project_details(request,pk):
    project=Project.objects.get(id=pk)
    tasks=project.Project_tasks.all()
    completed_tasks=project.Project_tasks.filter(completed=True)
    if tasks:
        progress=(len(completed_tasks)/len(tasks))*100
    else:
        progress=100

    context={
        'project':project,
        'tasks':tasks,
        'completed_tasks':completed_tasks,
        'progress':progress
        }
    return render(request,'main/project_details.html',context)


# the main login function
def login(request):
    if request.method=='POST':
        userName=request.POST['userName']
        password=request.POST['password']
        user = authenticate(username=userName, password=password)
        if user is not None:
            if user.last_login is None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('password_change'))
            auth_login(request, user)
            return HttpResponseRedirect(reverse('main'))

        else:
            messages.error(request,'username or password not correct')
            return HttpResponseRedirect(reverse_lazy('main'))


    return render(request,'main/login.html')



def mainLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('main'))






@login_required(login_url=reverse_lazy('mainLogin'))
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse_lazy('main'))
        else:
            messages.error(request,'password is in correct')
            return HttpResponseRedirect(reverse('password_change'))
    return render(request,'main/change-password.html')
