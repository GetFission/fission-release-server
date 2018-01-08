import uuid

from django.conf import settings
from django.db import models

from django_extensions.db import models as dj_models

from projects import models as project_models


class Release(dj_models.TimeStampedModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    project = models.ForeignKey(project_models.Project, blank=True, null=True)

    windows_artifact = models.FileField(null=True, blank=True)
    darwin_artifact = models.FileField(null=True, blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    def __str__(self):
        return '<Project: {}>'.format(self.name)

    def __repr__(self):
        return self.__str__()
