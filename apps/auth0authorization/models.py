from django.db import models
from django.conf import settings

from django_extensions.db import models as dj_models
import jsonfield


class Auth0LoginProfile(dj_models.TimeStampedModel):
    """Object to store profile data passed in when user logs in via Auth0
       Profile object will be payload from Google, Github or Auth0 auth
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='profile')
    profile = jsonfield.JSONField()

    def __str__(self):
        return str(self.profile.get('sub'))

    def __repr__(self):
        return self.__str__()
