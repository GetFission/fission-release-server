import uuid

from django.conf import settings
from django.db import models

import autoslug
from django_extensions.db import models as dj_models
from jsonfield import JSONField


class Project(dj_models.TimeStampedModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    api_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    slug = autoslug.AutoSlugField(populate_from='name', unique=True)

    rms_url = models.CharField(
        help_text='Repository Management Service (Github, Bitbucket, etc)',
        max_length=255, blank=True, null=True
    )


    def __str__(self):
        return '<Project: {}>'.format(self.name)

    def __repr__(self):
        return self.__str__()


class ProjectClient(dj_models.TimeStampedModel):
    project = models.ForeignKey(Project, blank=True, null=True, related_name='clients')
    uid = models.CharField(max_length=255)
    last_seen = models.DateTimeField(auto_now=True)
    last_version_sent = models.CharField(max_length=255, blank=True, null=True)
    last_version_sent_release_rule = models.ForeignKey(
        'releases.ReleaseRule', blank=True, null=True)  # Denotes the release rule for why the last version was sent
    last_version_seen = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)  # win32, darwin64, etc
    sysarch = models.CharField(max_length=255, blank=True, null=True)  # x64 vs ia32
    client_meta = JSONField(blank=True, null=True)  # Used to store data users want to associate with client

    def __str__(self):
        return f'<{self.project.name}/{self.uid}/{self.last_version_seen}>'

    def __repr__(self):
        return self.__str__()

