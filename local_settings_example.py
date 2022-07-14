# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Databases

DATABASES_LOGIN = {
    'default': {
        'NAME': '',
    },
}

# Static files

MEDIA_ROOT = 'media/'

# Security

CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = False
