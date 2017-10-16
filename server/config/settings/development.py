from config.settings import common


class Development(common.Common):
    ALLOWED_HOSTS = ['localhost']

    DEBUG = True

    PAGE_CACHE_SECONDS = 1

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'electronfission_dev',
            'USER': 'electronfission',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': 5432,
        }
    }

    # TODO AA Figure out a way to make this work
    # REST_FRAMEWORK['EXCEPTION_HANDLER'] = (
    #     'django_rest_logger.handlers.rest_exception_handler'
    # )

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'INFO',
            'handlers': ['django_rest_logger_handler'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                          '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'django_rest_logger_handler': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['django_rest_logger_handler'],
                'propagate': False,
            },
            'django_rest_logger': {
                'level': 'DEBUG',
                'handlers': ['django_rest_logger_handler'],
                'propagate': False,
            },
        },
    }

    DEFAULT_LOGGER = 'django_rest_logger'

    LOGGER_EXCEPTION = property(lambda x: x.DEFAULT_LOGGER)
    LOGGER_ERROR = property(lambda x: x.DEFAULT_LOGGER)
    LOGGER_WARNING = property(lambda x: x.DEFAULT_LOGGER)
