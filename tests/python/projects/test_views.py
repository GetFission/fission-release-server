import pytest

from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APIClient

from projects import models as project_models


@pytest.fixture
def client():
    client = APIClient()
    user = User.objects.create(username='foo')
    client.force_login(user)
    return client


@pytest.mark.django_db
def test_create_view(client):
    resp = client.post('/api/v1/projects/create/', {})
    assert resp.status_code == 400
    assert resp.json()['name'] == ["This field is required."]

    resp = client.post('/api/v1/projects/create/', {
        'name': 'Foo Project'
    })
    assert resp.status_code == 201
    expected_json = {
      'name': 'Foo Project', 'rms_url': None, 'slug': 'foo-project'}
    assert resp.json() == expected_json


@pytest.mark.django_db
def test_list_view(client):
    project_models.Project.objects.create(name='Bar')
    project_models.Project.objects.create(name='Baz', rms_url='exampe.com/foo/baz')

    resp = client.get('/api/v1/projects/list/')
    assert resp.status_code == 200
    assert resp.json()['results'] == [{}]
 