from distutils.command import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# from matplotlib import image
#this is not accessed here by mistake and messing up the production on the server 
from PIL import Image 
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
#this deletes all the user data if the user is deleted from the db 
    image = models.ImageField(default= 'default.jpg', upload_to = 'profile_pics')
    def __str__(self):
        return f"{self.user.username} profile lies here"

    def save(self, *args, **kwargs):
#args stands for arguments and kwargs for keyword arguments 
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
#the outputsize appears to be a var and its just a tuple (why not a lst??)



#here we are going to overrride the save method of the parent class. The super runs the save 
#method of the parent class and 
    

