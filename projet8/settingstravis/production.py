from . import *

DEBUG = False
ALLOWED_HOSTS = ['15.236.224.213']

DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cleaned',
        'USER': 'fostin',
        'PASSWORD': 'Hacksounet3*',
         'HOST': '',
        'PORT': '5432',
    }
}

STATICFILES_DIRS = [
    "/home/fostin/projet8/static"
]
