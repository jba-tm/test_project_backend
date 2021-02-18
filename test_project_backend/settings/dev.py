from ._base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WEBSITE_URL = "http://127.0.0.1:8000"  # without trailing slash

INSTALLED_APPS = INSTALLED_APPS + [
    # 'debug_toolbar',
]

MIDDLEWARE = MIDDLEWARE + [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

 # For development purposes.
CORS_ORIGIN_ALLOW_ALL = True

try:
    from .local import *
except ImportError:
    pass
