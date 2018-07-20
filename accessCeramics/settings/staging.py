"""
Staging deploy settings for accessCeramics.
"""

import os
import django_heroku

from accessCeramics.settings.base import *


# Secret key is set in Heroku environment variables
SECRET_KEY = os.getenv('SECRET_KEY')

# Turn off debug to mimic production
DEBUG = False

# JawsDB MySQL Heroku Addon
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.getenv('JAWSDB_URL'),
        'PORT': os.getenv('JAWSDB_PORT'),
        'NAME': os.getenv('JAWSDB_NAME'),
        'USER': os.getenv('JAWSDB_USER'),
        'PASSWORD': os.getenv('JAWSDB_PASS'),
    },
}

# Use heroku setup tool
django_heroku.settings(locals())
