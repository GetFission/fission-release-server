"""Django settings for fission project."""

import os
import sys

from configurations import Configuration, values

BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.dirname(__file__)))  # remove /sswmain/settings to get base folder

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, BASE_DIR)


class Common(Configuration):
    BASE_DIR = BASE_DIR

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'ajsdgas7&*kosdsa21[]jaksdhlka-;kmcv8l$#diepsm8&ah^'

    DEBUG = True

    ALLOWED_HOSTS = ['']

    # Application definition
    DJANGO_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.staticfiles',
        'django.contrib.messages',
        'django.contrib.sessions',
        'django.contrib.admin'
    )

    VENDOR_APPS = (
        'rest_framework',
        'knox',
        'django_extensions'
    )

    PROJECT_APPS = (
        'accounts',
        'base',
        'review_apps'
    )

    INSTALLED_APPS = DJANGO_APPS + VENDOR_APPS + PROJECT_APPS

    MIDDLEWARE_CLASSES = (
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.common.CommonMiddleware'
    )

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    ROOT_URLCONF = 'config.urls'

    WSGI_APPLICATION = 'config.wsgi.application'

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # TODO (Ahmed): investigate auth0
    AUTH_USER_MODEL = 'accounts.User'
    ACCOUNT_ACTIVATION_DAYS = 7  # days

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    # store static files locally and serve with whitenoise
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    # ############# REST FRAMEWORK ###################

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.BasicAuthentication',
        ),
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 20,
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.JSONParser',
            'rest_framework.parsers.FormParser',
            'rest_framework.parsers.MultiPartParser',
        ),
    }

    # ############ REST KNOX ########################
    REST_KNOX = {
        'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
        'AUTH_TOKEN_CHARACTER_LENGTH': 64,
        'USER_SERIALIZER': 'knox.serializers.UserSerializer'
    }

    # ####### Logging

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                          '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['sentry'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['sentry'],
                'propagate': False,
            },
        },
    }

    DEFAULT_LOGGER = 'console'

    LOGGER_EXCEPTION = DEFAULT_LOGGER
    LOGGER_ERROR = DEFAULT_LOGGER
    LOGGER_WARNING = DEFAULT_LOGGER
