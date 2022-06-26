#FIXED. There is work to do to learn how to pretty up the template but the ikkar function is there 
# finally time to fix the posts that dont show up. Which is a function of the veiws 
# and the home page 
# 
#SOLVE right now the login is redirecting to the home but im  not sure from the template why 
# and i cant find the login view  



#order of things that have to be done. 

#beofore can use admin have to create user which requires python manage.py migrate 
#python manage.py createsuperuser
#after creating an object in models run make migrations to create the table
#if you enter into cmd manage.py sqlmigrate (appname) 0001 which is the name of the file it will show you 
#the actual sql code 
#runing the migrate command actually creates the table which is in sqlite

#A URL slug is the part of the URL after the last backslash.