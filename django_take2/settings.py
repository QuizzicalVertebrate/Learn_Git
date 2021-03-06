#loaded a third party app crispy template for forms. pip install it add it to apps and changed the 
#defualt bootstrap class to 4 at the bottom of the file. hass to be lowercase when added to the app 
#or so i just found out 


from envvars import username
#nodemon gave issues with the from .envvars which i dont understand cuz its one level up in the parent 
#dir
"""
Django settings for django_take2 project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8zp&*-hq@$!fhh#p)q$mlv4z=%1btlvrdr1t%ecxswzv=g6d+$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#this was talked about on the pod its a security measure used to?? anwer it controls for 
# what servers are supposed to be running your files and blocks those rhat are not 
# .


# Application definition

INSTALLED_APPS = [
    'crispy_forms',
    'users.apps.UsersConfig',
    'blog.apps.BlogConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api.apps.ApiConfig',
    'corsheaders',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'allauth', 
    'allauth.account', 
    'allauth.socialaccount', 
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#lightweight software that handle requests and response 

CORS_ORIGIN_WHITELIST = (
'http://localhost:3000',
'http://localhost:8000',)

ROOT_URLCONF = 'django_take2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
#dict in list with a dict as the value of one of the keys of the og dict

WSGI_APPLICATION = 'django_take2.wsgi.application'
#path to the development server?? Does this need to be changed for prod? he didnt change it 


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ], 
    'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.TokenAuthentication',
    ],
}


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_REDIRECT_URL = 'blank'

#this i set and its the redirect after login so that you dont get the same form 

LOGIN_URL = "Login"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#this is the full path to where the media will be stored. Base dir is at the top of the settings 
#file up here 
#this sets the media root as in the base directory but with a dir in there called media 
# the os.path.join makes sure this works no matter what os you are on. ??? how  

MEDIA_URL = "/media/"

#this changes the route we are directed to when we try to access a page that we arent allowed 
#too if not logged in 

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND ='django.core.mail.backends.console.EmailBackend' 
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#Simple Mail Transfer Protocol SMTP is one of the most common ones alongside POP and IMAP.
# Specifically, an SMTP server handles the sending, receiving, and relaying of email

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587

# Those are the communication endpoints that handle the transfer of email data over SMTP as it 
# moves through a network, from one server to another. 


# EMAIL_USE_TLS = True 
# EMAIL_HOST_USER = username
#im inporting this from the env file 

# EMAIL_HOST_PASSWORD = 'zmgrdmypnyxoypgo'

SITE_ID = 1

#SITE_ID is part of the built-in Django ???sites??? framework86, which is a way to host multiple
#websites from the same Django project. We obviously only have one site we are working on here
# but django-allauth uses the sites framework, so we must specify a default setting.



