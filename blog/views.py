# from ssl import HAS_TLSv1
#this one too is the same mess
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from requests import post
from .models import Post
from django.views.generic import ListView
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView, 
    DeleteView
    
     )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]
      

def Home(request):
    context = {
        'posts':Post.objects.all()
        
                }
    
    return render(request, 'blog\Home.html', context)


def About(request):

    
    return render(request, "blog\About.html")


#inputting a the var as a third input to our render func allows the 

#that last var is a dict here cuz it was created as a dict earlier in the function rather than directly
#in the input. So ut seems you take need the dict. I wish there was a was to see from within vscode
#what args are permitted for any function. 

#LESSON when you get an error of s certain type just check that things arent doubled up before you check 
#complicated internet stuff 

class PostListView(ListView):
#remember that im creating the new class here even when using built in django stuff im just allowed 
#to inherit from listview here so i will already have methods
    model = Post

    template_name = 'post_list.html'

    var = {'posts': Post.objects.all()}

    context_object_name: var

    ordering = ['date']

    paginate_by: 5
#this is a paginator object which you van also use outisde of the class here but it sets a number
#of objects per page in listview

class PostDetailView(DetailView):
#remember that im creating the new class here even when using built in django stuff im just allowed 
#to inherit from listview here so i will already have methods
    model = Post

#here we wont specify a template and we will put it in the place where it will be default looked for. 


class PostCreateView(LoginRequiredMixin, CreateView):
#remember that im creating the new class here even when using built in django stuff im just allowed 
#to inherit from listview here so i will already have methods
    model = Post

    fields = ['title', 'post',]

    def form_valid(self, form):
        form.instance.author = self.request.user
#here we are ovveriding the natural save method which apparently is called form valid and setting 
#the author field as the logged in user which we created in models. You can also add the author field
#but that just ends up displaying all the authors to everyone. 
        return super().form_valid(form)
#to chap these things need the source code for the forms class, but it runningt he form valid method
#on the parent class cuz we reset it here we need to run it ourselves??

#the fields here are just the fields in the post objects 

#cant use decorators on classes so need some other way to make sure the post creator is logged in 
#so they have a thing 

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#the mixins need to be to the left of the updateview
#remember that im creating the new class here even when using built in django stuff im just allowed 
#to inherit from listview here so i will already have methods
    model = Post

    fields = ['title', 'post',]

    def form_valid(self, form):
        form.instance.author = self.request.user
#here we are ovveriding the natural save method which apparently is called form valid and setting 
#the author field as the logged in user which we created in models. You can also add the author field
#but that just ends up displaying all the authors to everyone. 
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
#i think this cracked the code on the multiple returns from functions where one is a conditional 
#and the other is not

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#remember that im creating the new class here even when using built in django stuff im just allowed 
#to inherit from listview here so i will already have methods
    model = Post

    success_url = 'blank'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserListView(ListView):
#remember that im creating the new class here even when using built in django stuff im just allowed 
#to inherit from listview here so i will already have methods
    model = Post

    template_name = 'blog/user_posts.html'

    context_object_name: Post.objects.all()

    ordering = ['date']

    paginate_by: 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
#NEEED THTE SECOND UNDERSCORE MUST LEARN HOW TO KNOW THESE THINGS. OTHER DIDNT FIND A MATCHING 
#SET NO IDEA WHY. Turns out her made an error. Oyyy
#this kwargs. get method gets info from the url here  it gets the username and checks it against 
#the db to see of there is such a user. If yes it gest the queryset for that user. If not, it returns
#a 404. We are also ovveriding the regular method that is built in which is why we need the super 
#method below 
        return Post.objects.filter(author = user).order_by('-date_posted')

    







