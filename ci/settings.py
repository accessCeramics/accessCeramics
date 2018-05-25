# This file gets called from the main settings.py when in a CI environment,
# so it can modify any of the settings in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

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

# Secret key gets generated and added to this file by travis - see .travis.yml
