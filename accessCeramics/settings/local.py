"""
Local development settings for accessCeramics.
"""

import os
import uuid

from accessCeramics.settings.base import *


# Generate a random secret key
SECRET_KEY = uuid.uuid4()

# Turn on debug output
DEBUG = True

# Use SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Enable the debug toolbar
INSTALLED_APPS += ['debug_toolbar']
