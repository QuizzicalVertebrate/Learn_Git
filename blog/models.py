#from the django pod. Serializer turns showing web pages into sending data usually json which is what 
#a API is. django rest api. There is also the cors. 

#to access the data in the db from the shell. 
#python manage.py shell
#than you need to import the classes user is where it is below in contrib and Post will be here in blog.
#models
#METHODS ARE 
#User.objects.all() gets a quesryset of users 
#User.objects.filter(username="")
#User.User.objects.all()
#if you capture an individual user in a var you get methods for the instance. So, instance vars. 
#var.id(where the user captured in the var is what the method is being called on)
#var.pk (private key)
#User.objects.get(id= relevant int) gets you the user by id 
#for your class (here its posts) you have 
#var = classname(here Post)(class fields with the proper types of input)
#so here it is post_1 = Post(post= "text", author= a user in the db, title = "text") no date cuz its auto
#you neeed to save after creating the objects. 
#can call objects.all() on the class as well presumably cuz of inheritence from Models
#cls cleans the shell exit() gets out of it 
#after creating a class object have to save it 
#after capturing a User in the var can use 
# user.(classname)_set.create(class fields) dont have to use the save after and dont have to input a user 
#var which has been bolluxing everything up. when creating this one the title is the title in the field 
#and not the var you define it in. 




from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    post = models.TextField(max_length=10000)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
#SUPER IMPORTANT the foriegn key here allows us to map other things to it so that if there are multiple posts
#they can all be put under this authors column?? in the table 
    date = models.DateTimeField(auto_now_add = True )
#the = True args are for a function that takes optional arguments 
    title = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse ('post-detail', kwargs= {'pk':self.pk})
    

    def __str__(self):
        return self.title

