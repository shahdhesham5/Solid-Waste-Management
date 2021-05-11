from django.shortcuts import render,  redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
from .decorators import allowed_users ,admin_only ,unauthenticated_user
from django.contrib.auth import login as original_login, authenticate, logout
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages

from django.db import models

User = get_user_model()
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

def login(request):
	if request.user.is_authenticated:
		return redirect('new')
	else:
		return render(request, 'sw/templates/templates/login.html')


def sw_login(request):
	if request.user.is_authenticated:
		return redirect('new')
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:
					original_login(request, user)
					return redirect('new')
			else:
				 messages.error(request,'username or password not correct')
				 return redirect('login')
	return redirect('login')




def sw_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse_lazy('login'))


def signup(request):
	if request.user.is_authenticated:
		return  HttpResponseRedirect(reverse_lazy('new'))
	else:
		form = CreateUserForm()
		template_name ="sw/templates/templates/signup.html"
		if request.method == 'POST':

			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				raw_password = form.cleaned_data.get('password1')
				messages.success(request, 'Account was created for ' + user)
				user_created = authenticate(username=user, password=raw_password)
				original_login(request,user_created)
				return  HttpResponseRedirect(reverse_lazy('new'))
		context = {'form':form}
		return render(request, 'sw/templates/templates/signup.html', context)
	# form=UserCreationForm()
	# if request.method=="POST":
	# 	form=UserCreationForm(request.POST)
	# 	form.save()
	# context = {'form':form}
	# return render(request, 'sw/templates/templates/signup.html',context)
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    #     form = CreateUserForm()
    #     if request.method == 'POST':
	# 		form = CreateUserForm(request.POST)
	# 		if form.password1:
	# 			return HttpResponse(form)
	# 		else:
	# 			return HttpResponse(form.username)
	#
	# 		if form.is_valid():
	#
	# 			form.save()
	# 			user = form.cleaned_data.get('username')
	# 			messages.success(request, 'Account was created for ' + user)
	# 			return render(request, 'sw/templates/templates/login.html')
	# 		else:
	# 			return 	 HttpResponse("Not Valid")
    #     context = {'form':form}
    #     return render(request, 'sw/templates/templates/signup.html',context)

def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse_lazy('sw_login'))
	else:
		return render(request, 'new.html')


def dashboard(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
     return render(request, 'sw/templates/templates/dashboard.html')



def map(request):
        if not request.user.is_authenticated:
            return render(request, 'sw/templates/templates/login.html')
        else:
            groupNames=[group.name for group in request.user.groups.all()]
            # for group in request.user.groups.all():
            #     groupNames.append(group.name+" ")

            if 'Supervisors' in groupNames:
                return render(request, 'sw/templates/templates/mapexample.html')
            elif 'Drivers' in groupNames :
                return render(request, 'sw/templates/templates/mapdriver.html')
            else:
                # return HttpResponse("You are Not Authorised")
                messages.error(request,'You are Not Authorised')
                return render(request, 'sw/templates/templates/login.html')
                




#test
def database(request):
    return render(request, 'sw/templates/templates/database.html')

def ads(request):
    return render(request, 'sw/templates/templates/ads_mangment.html')

def properties(request):
    return render(request, 'sw/templates/templates/countery_properties.html')

def data(request):
    return render(request, 'sw/templates/templates/data_collection.html')

def historical(request):
    return render(request, 'sw/templates/templates/historical_cairo.html')

def public(request):
    return render(request, 'sw/templates/templates/public_participation.html')

def swm(request):
    if not request.user.is_authenticated:
        return render(request, 'sw/templates/templates/login.html')
    else:
        return render(request, 'sw/templates/templates/solid_waste_managment.html')

# @allowed_users(allowed_roles=['anonymous'])
# @unauthenticated_user
# @admin_only
def test(request):
    if not request.user.is_authenticated:
        return render(request, 'sw/templates/account/login.html')
    else:
        groupNames=[]
        for group in request.user.groups.all():
            groupNames.append(group.name+" ")

        if 'drivers' in groupNames:
            return HttpResponse("I am driver")
        else :
            return HttpResponse(groupNames)



        # return HttpResponse(group)

    # if not request.user.is_authenticated:
    #     return HttpResponse("I am not login")
    # else:
    #     return HttpResponse("I am login")
