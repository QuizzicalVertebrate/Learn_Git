from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'


#this is the mystery of how we create the signals 

class UsersConfig(AppConfig):
    name = 'users'
    def ready(self):
        import users.signals 

#it works now. Not sure how. Added default_app_config = 'users.apps.UsersConfig' to the init
#file and the class here. Have to think thru the lomdus. Appconfig is itself a class. Here 
#usrconfig inherits methods from appconfig. Looks like im creating a new class of usersconfig 
#which has this method wich takes self and imports signals. Seems that userconfig jsut imports
#the signals. Not at all clear what is happening here??
