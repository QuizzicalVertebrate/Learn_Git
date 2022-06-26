from django.db import models
from pkg_resources import require

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=250, blank=True)
    subtitle = models.CharField(max_length=250, blank=True)
    author = models.CharField(max_length=100, blank=True)
    isbn = models.CharField(max_length=13, blank=True)
    # class Meta():
    #     app_label = 'api'

#this is a wild thing i just got from the internet but it works. Have no idea what the issue was 
#it solves Model class api.models.Book doesn't declare an explicit app_label and isn't in an 
# application in INSTALLED_APPS. Was really cuz I didnt put the new app api into the settings.py 
# list.
    
    
    def __str__(self):
        return self.title
