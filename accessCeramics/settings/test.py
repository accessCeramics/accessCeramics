"""
CI test settings for accessCeramics.
"""

import os
import uuid

from accessCeramics.settings.base import *


# Generate a random secret key
SECRET_KEY = uuid.uuid4()

# Turn on debug output
DEBUG = False

# Test against MySQL in CI
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'HOST': 'localhost',
        'PORT': '',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        },
    },
}

