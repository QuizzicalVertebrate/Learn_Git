from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#this sends a signal when a user profile is saved and than we are goingt to want to do somthing with 
#that 


@receiver(post_save, sender= User)
def Create_Profile(sender, instance, created, **kwargs ):
    if created:
        Profile.objects.create(user= instance)
#this is a function that we want to run whenever a user is created. But to do that we need to use
#a decorator at the top which always adds functionality to a function. The sender is defined in the 
#end of the decorator, here it is User. It is recieved by the reciever and activates the function 
#the function checks for created and than creates a profile. We are running create on the objects
#of the profile class. This is to create a profile which is not naturally tied to users cuz we 
#create the profile class 

@receiver(post_save, sender= User)
def Save_Profile(sender, instance, **kwargs ):
        instance.profile.save()