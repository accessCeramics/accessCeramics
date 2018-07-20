"""
Staging deploy settings for accessCeramics.
"""

import os
import django_heroku

from accessCeramics.settings.base import *


# Secret key is set in Heroku environment variables
SECRET_KEY = os.environ['SECRET_KEY']

# Turn off debug to mimic production
DEBUG = False

# JawsDB MySQL Heroku Addon
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ['JAWSDB_URL'],
        'PORT': os.environ['JAWSDB_PORT'],
        'NAME': os.environ['JAWSDB_NAME'],
        'USER': os.environ['JAWSDB_USER'],
        'PASSWORD': os.environ['JAWSDB_PASS']
    },
}

# Use heroku setup tool
django_heroku.settings(locals())
