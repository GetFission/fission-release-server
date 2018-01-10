from django.contrib import admin

from releases import models


# class RelaseAdmin(admin.ModelAdmin):
#     fields = ['name', 'rms_url', 'slug', 'api_key']
#     readonly_fields = ['slug', 'api_key']

admin.site.register(models.Release)
