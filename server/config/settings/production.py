from configurations import values

from config.settings import common


class Production(common.Common):
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG

    PAGE_CACHE_SECONDS = 60

    # TODO: n a real production server this should have a proper url
    ALLOWED_HOSTS = ['*']

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecreteValue()

    DATABASES = values.DatabaseURLValue()

    # TODO fix
    # REST_FRAMEWORK['EXCEPTION_HANDLER'] = 'django_rest_logger.handlers.rest_exception_handler'  # NOQA (ignore all errors on this line)


    # ########### Sentry configuration

    # Change this to proper sentry url.
    RAVEN_CONFIG = {
        'dsn': '',
    }

    # INSTALLED_APPS = INSTALLED_APPS + (  # NOQA (ignore all errors on this line)
    #     'raven.contrib.django.raven_compat',
    # )
 
    DEFAULT_LOGGER = 'raven'

