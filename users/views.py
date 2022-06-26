import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from . import views
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth.views import PasswordResetView
#at the wonderful website in the autism file find where to import from at the top 

# Create your views here.

#redirecting to anything other than the register page in the templates here got a no https response type 
#error and I think thats because 


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('Login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


#this creates this form in our system if we get data which we will now need to validate else empty form 
#and than flashes a message. There are many types of flash messages. And than after that we will redirect 


@login_required
def Profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
    #the func is called the form here is passed to the webpage thru the dict but now it is passed with 
    #the info of the request object which somehow encodes the logged in user. The requesT here
    #is going to be a GET 
    #the request.post passes in the post data. which i think is going to be the new data. 
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f"YOU DID IT, {username}  NOW REAP THE WHIRLWIND")
            return redirect ("Profile")
    #the redirect over here gets you back to the page without the error message of form resubmission
    #which is caused by sending two post requests after each other here it will be a GET request from 
    #the server for the profile page which will have the new profile info cuz its now the relevant 
    #stuff in the db. When did the old stuff get deleted??

    else:
        u_form = UserUpdateForm(instance=request.user)
    #the func is called the form here is passed to the webpage thru the dict but now it is passed with 
    #the info of the request object which somehow encodes the logged in user. The requesT here
    #is going to be a GET 
    #the request.post passes in the post data. which i think is going to be the new data. 
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form':u_form,
            'p_form':p_form
        }
    return render(request, r'C:\Coding\Environments\django_take2\users\templates\Profile.html', context)

class NewPasswordResetView(PasswordResetView):
    
    pass
