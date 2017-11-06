from django.db import models
from django_extensions.db import models as dj_ext_models


class VisitorEmail(dj_ext_models.TimeStampedModel):
    email = models.EmailField()


    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'{self.email}'
