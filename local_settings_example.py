SECRET_KEY = ''

DEBUG = True

ALLOWED_HOSTS = ['*']
USE_X_FORWARDED_PORT = False

# Databases

DATABASES_LOGIN = {
    'default': {
        'USER': '',
        'PASSWORD': '',
        'NAME': '',
        'HOST': '',
        'PORT': '',
    },
}

# Static files

MEDIA_ROOT = 'media/'

# Security

CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = False

# DRF

API_ROOT = 'api/'
