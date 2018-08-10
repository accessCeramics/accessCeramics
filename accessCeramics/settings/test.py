# pylint: disable=W0614, W0401
"""
CI test settings for accessCeramics.
"""

import os
import uuid

from accessCeramics.settings.base import *


# Generate a random secret key
SECRET_KEY = str(uuid.uuid4())

# Turn on debug output
DEBUG = False

# Test against MySQL in CI
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'HOST': 'localhost',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        },
    },
}

