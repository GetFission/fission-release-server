from django.contrib import admin

from projects import models

class ProjectAdmin(admin.ModelAdmin):
    fields = ['name', 'rms_url', 'slug', 'api_key']
    readonly_fields = ['slug', 'api_key']

admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ProjectClient)
