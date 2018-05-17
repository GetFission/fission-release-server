# import uuid

from django.conf import settings
from django.db import models

from django_extensions.db import models as dj_models
import jsonfield

from projects import models as project_models


class Release(dj_models.TimeStampedModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    project = models.ForeignKey(project_models.Project, blank=True, null=True)

    # Todo: investigate windows artifacts (nsis, squirrel, nuget, etc..)
    windows_artifact = models.FileField(null=True, blank=True)

    # Produced by electron builder. Mac zip-file is needed for auto-update
    darwin_zip = models.FileField(null=True, blank=True)
    darwin_zip_sha512 = models.TextField(blank=True, null=True)
    darwin_dmg = models.FileField(null=True, blank=True)
    darwin_dmg_sha512 = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    def get_darwin_release_files(self):
        res = []
        if self.darwin_zip:
            res.append({
                'url': self.darwin_zip.url,
                'sha512': self.darwin_zip_sha512
            })
        if self.darwin_dmg:
            res.append({
                'url': self.darwin_dmg.url,
                'sha512': self.darwin_dmg_sha512
            })
        return res

    def __str__(self):
        return '<{}/{}/{}>'.format(self.project.name, self.version, self.name)

    def __repr__(self):
        return self.__str__()


class ReleaseRule(dj_models.TimeStampedModel):
    release = models.ForeignKey(Release, blank=True, null=True)
    project = models.ForeignKey(
        project_models.Project,
        blank=True, null=True,
        related_name='release_rules'
    )
    is_darwin = models.BooleanField(default=False)

    is_windows = models.BooleanField(default=False)
    is_linux = models.BooleanField(default=False)
    channel = models.CharField(max_length=255, blank=True, null=True)
    darwin_percent = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)
    windows_percent = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)
    linux_percent = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)

