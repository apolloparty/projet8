import os

"""
Django settings file for you project.
"""

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ['DATABASE_NAME'],
    'USER': os.environ['DATABASE_USER'],
    'PASSWORD': os.environ['DATABASE_PASSWORD'],
    }
}

DATABASE_NAME = 'test_db'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = ''
