from django.contrib import admin

from auth0authorization import models


admin.site.register(models.Auth0LoginProfile)
