from ._base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = os.environ.get("CORS_ORIGIN_WHITELIST").split(" ")

try:
    from .local import *
except ImportError:
    pass
