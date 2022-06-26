"""django_take2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth import views as auth_views
from users import views as users_views
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, 
PasswordResetConfirmView, )
from django.urls import reverse_lazy
from rest_framework.schemas import get_schema_view
from rest_framework import permissions # new
from drf_yasg.views import get_schema_view # new
from drf_yasg import openapi 

schema_view = get_schema_view( # new
openapi.Info(
title="Blog API",
default_version="v1",
description="A sample API for learning DRF",
terms_of_service="https://www.google.com/policies/terms/",
contact=openapi.Contact(email="hello@example.com"),
license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=(permissions.AllowAny,))




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls') ),
    path('Registration/',users_views.register, name="Register-Page"),
    path('Profile/',users_views.Profile, name="Profile"),
    path('Login/',auth_views.LoginView.as_view(template_name= 'users\login.html'), name="Login"),
    path('Logout/',auth_views.LogoutView.as_view(template_name= 'users\logout.html'), name="Logout"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='blog/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='blog/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='blog/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='blog/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('', include('blog.urls')),
#the password reset confirm needs the uidb64 user id in 64 bits and also needs the token
#these last two here are whats called class based views
#we feed the optional arg template name into the view cuz otherwise the default is a subdirectory of the 
#users/regitsration and we dont want to do that rn 
    path('api/v1/', include('api.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('openapi', get_schema_view(
        title="Blog API",
        description="A sample API for learning DRF",
        version="1.0.0"
        ), name='openapi-schema'),
    
    path('swagger/', schema_view.with_ui( # new
    'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui( # new
    'redoc', cache_timeout=0), name='schema-redoc'),


]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#the include function chops off evrything that has been matched already and send the rest to 
# wherever is indicated. Here that is blog which is our app file. urls which is the file thats 
# been created there

#need to tell Django to also take routes from our app. This is the project level dir. The idea 
#is that you might want to use the same app in multiple projects so they are created separate. 

#if you put in an empty route on localhost with the setting of the include path as a full path you will
#get nothing 

#the reason to do it with a main file is so that you can change all the downstream routes with one change 

#cant easily just put urls here cuz than you have to somehow import the views file which is in a diff 
#folder 



