# pylint: disable=W0614, W0401
"""
Local development settings for accessCeramics.
"""

import os
import uuid

from accessCeramics.settings.base import *


# Generate a random secret key
SECRET_KEY = str(uuid.uuid4())

# Turn on debug output
DEBUG = True

# Use local MySQL in development; setup can be customized with envvars
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('ACCESSCERAMICS_DB_NAME', 'accessceramics'),
        'USER': os.getenv('ACCESSCERAMICS_DB_USER', 'root'),
        'PASSWORD': os.getenv('ACCESSCERAMICS_DB_PASS', 'accessceramics'),
        'PORT': os.getenv('ACCESSCERAMICS_DB_PORT', '3306'),
        'HOST': '127.0.0.1',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        },
    },
}

# Enable the debug toolbar
INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
