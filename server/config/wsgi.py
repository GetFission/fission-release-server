"""
WSGI config for django-react-redux-base project.

"""
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


os.environ.setdefault("DJANGO_CONFIGURATION", "Production")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# NOTE: Use configurations package to create wsgi application
from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()


from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
