#Configuration#

##STEP 1##
Add 'rating' to INSTALLED_APPS such as:

```
#!python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #....
    'rating'
)

```

##STEP 2##
Add following lines to settings.py

```
#!python

#Rating configuration
RATING_DRIVER = 'redis'
RATING_DRIVER_HOST = 'localhost'
RATING_DRIVER_PORT = 6379
RATING_DRIVER_DB = '0'
RATING_DRIVER_USER = ''
RATING_DRIVER_PASS = ''

```
