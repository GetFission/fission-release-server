import uuid

from django.conf import settings
from django.db import models

import autoslug
from django_extensions.db import models as dj_models


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
