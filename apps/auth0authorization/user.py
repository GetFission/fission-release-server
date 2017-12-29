import logging

from django.contrib.auth import get_user_model

from auth0authorization import models


log = logging.getLogger('apps.auth0authorization')


def clean_username(username):
    return username.replace('|', '.')


def jwt_get_username_from_payload_handler(payload):
    User = get_user_model()

    username = clean_username(payload.get('sub'))
    user, created = User.objects.get_or_create(username=username)

    # Update user email
    user.email = payload.get('email') or user.email
    user.save()

    profile, _ = models.Auth0LoginProfile.objects.get_or_create(user=user)
    profile.profile = payload
    profile.save()

    log.info('Is User just created?: {}'.format(created))
    log.info('User logged in with payload: {}'.format(payload))

    return username
