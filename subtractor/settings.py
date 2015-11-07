"""
Django settings for subtractor project.


Generated by 'django-admin startproject' using Django 1.8.4.


For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ADDING TO FIX WORKER REDIS ERROR (MAY NEED TO REMOVE..)
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "subtractor.settings") 
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cm7s+0(u*)se5+uuooo_-vi8n@&ivt&3zmj=zv4)a^=p$m6qp!'



# SECURITY WARNING: don't run with debug turned on in production!
if 'LOCAL_RUNNING' in os.environ:
    DEBUG = True
else:
    DEBUG = False

# DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']  #CHANGE FOR PRODUCTION!

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'audio_process',
    'bootstrap3',
     'django_rq',
     'gunicorn'

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'subtractor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'audio_process/templates/audio_process')],

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

WSGI_APPLICATION = 'subtractor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'subtractor',
    		'USER': 'django_user',                   
            'PASSWORD': 'deadmau5',              
            'HOST': 'localhost',                      
            'PORT': '5432',  
        }
    }
    # DATABASES = {}
    # #FROM OFFICIAL DJANGO DOCS, PUT BACK?
    # DATABASES['default'] =  dj_database_url.config()
else:
    DATABASES = {}
    #FROM OFFICIAL DJANGO DOCS, PUT BACK?
    DATABASES['default'] =  dj_database_url.config()


    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'America/Los_Angeles' #'UTC'


USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = 'staticfiles'
# STATIC_ROOT = 'static'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        # 'PASSWORD': 'some-password',
        'DEFAULT_TIMEOUT': 360,
    },
    'high': {
        'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379'), # If you're on Heroku
        'DB': 0,
        'DEFAULT_TIMEOUT': 500,
    },
    'low': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    }
}


# if DEBUG or TESTING:
#     for queueConfig in RQ_QUEUES.itervalues():
#         queueConfig['ASYNC'] = False


# CHANGE FOR PRODUCTION!
# SECRET_KEY = 'v5i%t-2)!&uateyb7jzml%k8@fgo4fxgb#2@1!7gmce40%yc@&'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

