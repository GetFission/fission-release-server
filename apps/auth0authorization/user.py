from django.contrib.auth import get_user_model


def clean_username(username):
    return username.replace('|', '.')


def jwt_get_username_from_payload_handler(payload):
    User = get_user_model()
    username = clean_username(payload.get('sub'))
    email = payload.get('email') or username + '@foo.com'

    user, created = User.objects.get_or_create(
        username=username,
        email=email
    )

    if created:
        print('new user here...', user)
    else:
        print('old user coming back', user)

    return username
