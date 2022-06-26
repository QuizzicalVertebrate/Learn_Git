from django.urls import path
from requests import post
from . import views
from .views import (
    
    PostDeleteView,
    PostListView, 
    PostDetailView,
    PostCreateView, 
    PostUpdateView,
    PostDeleteView,
    UserListView,
)




urlpatterns = [
    path('home/', views.Home, name="blog-home"),
    path('about/', views.About, name='blog-about'),
    path('', views.Home, name='blank'),
    path('Test', PostListView.as_view(), name='Test'),
#if we need to create a route that has multiple pieces like a blog view
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserListView.as_view(), name='User-View'),

#if you have a blank path w/0 the / it worls with blank and if with the / it does not 
    
] 
#when using class based views you need to convert the class to view by adding ._asview() and calling
#it
#this will look for templates in a specific place. But we can just change where its looking in views 
#when the urls are going to be accessed in templates its better to do that as the name rather than to hard
#code that way it changes with the url as it changes which if you think about it is basically a level of 
#abstraction


