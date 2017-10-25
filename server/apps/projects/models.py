import uuid

from django.db import models

from django_extensions.db import models as dj_models


class Project(dj_models.TimeStampedModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    api_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return '<Project: {}>'.format(self.name)

    def __repr__(self):
        return self.__str__()
