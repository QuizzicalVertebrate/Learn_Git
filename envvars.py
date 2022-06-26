#in control panel on windows system setttings system advances syetem setting 
# system properties env varaibles. Btw if you ever cant find the right file even in windows
# you can just inout the path. Game changer. 
# #you can store these on your local system and than access them onlu from the os  

import os 
gmail_app_password = os.environ.get('gmail_app_password')
#get method works cuz this is a dict no idea how you could know that

first_name = 'Coding'
last_name = 'Learning'
username = 'learntocodefast0'
password = 'Sun1fall'
phone_num = '0546413420'
birthday = 'Reg bd'
Gender = 'rather not say' 
app_password = 'zmgrdmypnyxoypgo'
linode_root_password = 'Sun1fall'
ssh_root_linode = 'ssh root@172.105.101.49'
hostname = 'django-server'
limiteduser = 'aviezer'
password = 1234
config_file = 'djang0_take2.conf'



#deployment 
#set up a new non root user for the server and used ssh thatuser@root num to get into it 
# pwd prints working dir 
# mkdir -p creates whole directory tree
# ~ means home folder
# make a ssh folder in the home dir. something to do with security
# created a new file on the server (remember the server is just a computer that holds a copy 
# of) a cool key pair we created so that we can log in securely from my home linux machine to the 
# server without a password
# changing permissions in linux
# there is a way to than disallow root access and disallow access without the keys imma not do that 
# cuz the no password thing ddint work
# updating the server rules to alolow specific types of traffic apparently http and ssh are diff 
# and allowing specific ports
# all of this is after starting a ufw firewall and setting it 
# requirements.txt file with all the things that are needed for the thing to work 
# pip freeze gives you all of your dependencies we copy that info into a requirements.txt file 
# and put that in the django project in my case i think it picked up everything i have installed cuz 
# its not in a a venv 
# can use bash to ge the project onto the server but if not can use git or filezilla
# the dirs in linuz arent the same as windows so ls may show nothing from home
# /mnt/c gets you into the c drive on the windows 
# -r means recursive copy means i can copy a dir 
# deployment got messed up cuz of all sorts of rando stuff that ended up in the txt file 
# goimg to have to do it manually 
# have to add the ip to the allowedhosts 
# 
# sudo anp- | grep apache checks if apache is running 
# /etc/apache2/sites-available/ holds the default conf files for apache i want to copy one 
# and use it for my own rename it use cp to copy and give it a name 
# SOLVED AN ISSUE when starting site need to use the name of the .conf file in sites-aailable 
# which here by mistake was the djang0_take2
# chown is change owner 
# 
# Understanding schema and models many to many lookups etc 
# 
# it creates a Pipfile containing software dependencies and a Pipfile.lock for ensuring
#  deterministic builds. “Determinism” means that each and every time you download the software 
# in a new virtual environment, you will have exactly the same configuration.
# .


