# from django.core.urlresolvers import reverse
import pytest
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_view():
    user = User.objects.create(username='foo')

# pytestmark = pytest.mark.django_db

# @pytest.mark.django_db
# class ProjectViewsTestCase(APITestCase):
#     pytestmark = pytest.mark.django_db
#     def setUp(self):
#         self.user, _ = User.objects.create(username='foo')
#         self.client.force_login(self.user)

#     def test_create_project(self):
#         resp = self.client.post('/api/projects/create', {})
#         print(resp)
