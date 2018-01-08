import os

import pytest
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient

from projects import models as project_models

from releases import models as releases_models


DATA_DIR = os.path.dirname(__file__)


@pytest.fixture
def user():
    user = User.objects.create(username='foo')
    return user


@pytest.fixture
def project():
    project, _ = project_models.Project.objects.get_or_create(name='foo')
    return project


@pytest.fixture
def client(user):
    client = APIClient()
    client.force_login(user)
    return client


@pytest.mark.django_db
def test_create_view_invalid(client, project):
    resp = client.post('/api/v1/releases/create/', {})
    assert resp.status_code == 400
    assert resp.json()['version'] == ["This field is required."]


@pytest.mark.django_db
def test_create_view_valid(client, project):
    resp = client.post('/api/v1/releases/create/', {
        'name': 'alpha',
        'version': '1.1.1',
        'darwin_artifact': open(os.path.join(DATA_DIR, 'data/darwin_test_file.txt')),
        'windows_artifact': open(os.path.join(DATA_DIR, 'data/windows_test_file.txt')),
        'project': project.id
    })

    print(resp.json())
    assert resp.status_code == 201

    expected_json = {'name': 'alpha', 'version': '1.1.1', 'project': project.id}
    res_json = resp.json()
    darwin_artifact_path = res_json.pop('darwin_artifact')
    windows_artifact_path = res_json.pop('windows_artifact')
    assert 'amazonaws.com' in darwin_artifact_path
    assert 'amazonaws.com' in windows_artifact_path
    assert res_json == expected_json

    resp = client.post('/api/v1/releases/create/', {
        'name': 'alpha',
        'version': '1.1.1',
        'darwin_artifact': open(os.path.join(DATA_DIR, 'data/darwin_test_file.txt')),
        'project_slug': project.slug
    })

    # assert resp.status_code == 201


# @pytest.mark.django_db
# def test_list_view(client, user):
#     # create 2 projects, one of which ish owned by current logged in user
#     project_models.Project.objects.create(name='Bar', created_by=user)
#     project_models.Project.objects.create(name='Baz', rms_url='exampe.com/foo/baz')

#     resp = client.get('/api/v1/projects/list/')
#     assert resp.status_code == 200
#     assert resp.json()['results'] == [
#         {'name': 'Bar', 'rms_url': None, 'slug': 'bar'}]
 
#     assert resp.json()['count'] == 1
