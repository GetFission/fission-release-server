from configurations import values

from config.settings import common


class CI(common.Common):
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG

    PAGE_CACHE_SECONDS = 60

    ALLOWED_HOSTS = ['*']

    DATABASES = values.DatabaseURLValue()

 
