# from django.test import TestCase
import pytest

from django.contrib.auth.models import User

from auth0authorization import user, models


@pytest.fixture
def github_payload():
    return {
        'nickname': 'SimplyAhmazing',
        'name': 'ahmad19526@gmail.com',
        'picture': 'https://avatars0.githubusercontent.com/u/1294344?v=4',
        'updated_at': '2017-12-29T01:01:17.581Z',
        'email': 'ahmad19526@gmail.com',
        'email_verified': True,
        'iss': 'https://getfission.auth0.com/',
        'sub': 'github|1294344',
        'aud': 'ev0a7ZjmcbPIadVw1an0N02CIVhn7kFd',
        'iat': 1514509277,
        'exp': 1514545277,
        'at_hash': 'SBQGyr2TGznipLCU-rYOOg',
        'nonce': 'UdhRfHNfbpNZ0279A2tBayquIIaTJ750'
    }


@pytest.fixture
def google_payload():
    return {
        'at_hash': 'LO-RBCuu8qh8m3oZ1vQizQ',
        'aud': 'ev0a7ZjmcbPIadVw1an0N02CIVhn7kFd',
        'email': 'ahmad19526@gmail.com',
        'email_verified': True,
        'exp': 1514538602,
        'family_name': 'Abdalla',
        'gender': 'male',
        'given_name': 'Ahmed',
        'iat': 1514502602,
        'iss': 'https://getfission.auth0.com/',
        'locale': 'en',
        'name': 'Ahmed Abdalla',
        'nickname': 'ahmad19526',
        'nonce': 'EIiSxbzjE6FZCw533uY2QgOecUD6h.ca',
        'picture': 'https://lh4.googleusercontent.com/-uv-x28H1Jlc/AAAAAAAAAAI/AAAAAAAAKDc/Ccnp9_tvy6M/photo.jpg',
        'sub': 'google-oauth2|104869273766969262589',
        'updated_at': '2017-12-28T23:10:02.705Z'
    }


@pytest.fixture
def auth0_payload():
    return {
        'at_hash': '_5Ix3HTpDObksSd1XGyJEA',
        'aud': '3noCCWzrdQyu8l2v8yGXuEMHOU5TgLrp',
        'email': 'simplyahmazing+1@gmail.com',
        'email_verified': False,
        'exp': 1514476118,
        'iat': 1514440118,
        'iss': 'https://electron-fission.auth0.com/',
        'name': 'simplyahmazing+1@gmail.com',
        'nickname': 'simplyahmazing+1',
        'nonce': 'ujTS8gG-uqkZt7ObS7dicpVKL-j0SLEd',
        'picture': 'https://s.gravatar.com/avatar/55102e90e4ab035950bd07cb9fecc689?s=480&r=pg&d=https%3A%2F%2Fcdn.auth0.com%2Favatars%2Fsi.png',
        'sub': 'auth0|5a447b499252727ec97938b1',
        'updated_at': '2017-12-28T05:48:38.774Z'
    }


@pytest.mark.django_db
def test_jwt_get_username_from_payload_handler_github(github_payload):
    username = user.jwt_get_username_from_payload_handler(github_payload)
    expected_username = user.clean_username(github_payload.get('sub'))
    assert username == expected_username

    _user = User.objects.get(username=expected_username)
    assert _user and _user.profile


@pytest.mark.django_db
def test_jwt_get_username_from_payload_handler_google(google_payload):
    username = user.jwt_get_username_from_payload_handler(google_payload)
    expected_username = user.clean_username(google_payload.get('sub'))
    assert username == expected_username

    _user = User.objects.get(username=expected_username)
    assert _user and _user.profile


@pytest.mark.django_db
def test_jwt_get_username_from_payload_handler_auth0(auth0_payload):
    username = user.jwt_get_username_from_payload_handler(auth0_payload)
    expected_username = user.clean_username(auth0_payload.get('sub'))
    assert username == expected_username
    assert User.objects.get(username=expected_username)

    _user = User.objects.get(username=expected_username)
    assert _user and _user.profile
