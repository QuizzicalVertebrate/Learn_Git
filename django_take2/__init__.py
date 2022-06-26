#FIX 
#SOLVE THE TEMPLATES ARENT RENDING CUZ ITS LOOkING IN USERS AND GETTING ONLY EITHER TOO FEW 
# STEPS DOWN OR THE RIGHT NUMBER OF STEPS BUT THE WRONG TREE.
#the slashes are wrong for the user templates
#registration is looking in blogs
#login has a slash wrong
#logout is looking in the right place but has the slash wrong
#when working with the local project it checks both apps but somehow knows to check the right
# subdir where the template is at least for login which was initially in users and for new/post
# that was initially in blog it checked in both users and blog for temmplates users for login and 
# blog for new/post.

#FIXED redirected to Login by changing the view redirect register page doesnt redirect after success 
#SOLVE the default profile pic doesnt work 
#SOLVE im not capturing the data from the class based views changing the code block for the for loop 
#to object_list worked but the ikkar is to know how to access all the attributs which i dont know
#FIXED by fixing the apps and init files with something profile is not being created when a user 
# is created off the internet
#SOLVE reverse match not found for the Passworddone page 
#SOLVE why is my email password being printed to the terminal twice on sever startup 
#SOLVE  author header on posts is sending to the logged in user not eh author profile and 
#lav davka does the logged in user have authoirty to visit that profile 

# Informational responses (100–199)
# Successful responses (200–299)
# Redirection messages (300–399)
# Client error responses (400–499)
# Server error responses (500–599)

#an HTML “widget” - a piece of user interface machinery
#there is lomdus here. When the view is linked to a URL its used in two directions. It sends
#the template to the browser  but is also sent to. Both a post and a get request are the url 
#sending things too the view. And a guess when it sends things back thats a post request to the 
#browser?

#THE IMPORT BEYOND TOP LEVEL IS CUZ IT HAS TO BE A PACKAGE (WITH AN INIT) RATHER THAN A MODULE 
#FOR THE PYTHON TO FIND IT 
