from django.test import override_settings
from rest_framework.test import APITestCase

from projects import models as project_models


@override_settings()
class ReviewAppsTestCase(APITestCase):
    def setUp(self):
        self.project = project_models.Project.objects.create(name='Test Project')

    def test_post_build_ping(self):
        valid_post_data = { "ci": "appveyor",
                 "platform": "win32",
                 "branch_name": "master",
                 "build_url": "example.com/foo/123",
                 "commit_hash": "123456",
                 "ci_job_id": "22",
                 "app_version": "1.4.5",
                 "pull_request_number": "33",
                 "api_key": str(self.project.api_key)
        }
        resp = self.client.post('/review-apps/', valid_post_data)
        assert resp.status_code == 201
        assert resp.status_text == 'Created'

        res = resp.json()
        res.pop('id')  # remove id
        res.pop('created')  # remove created time stamp

        expected = {'project': self.project.id, **valid_post_data}
        expected.pop('api_key')
        assert expected == res


        invalid_post_data = valid_post_data
        invalid_post_data.pop('api_key')
        resp = self.client.post('/review-apps/', invalid_post_data)
        assert resp.status_code == 400
        assert resp.status_text == 'Bad Request'
        assert resp.json() == {'api_key': ['This field is required.']}

        invalid_post_data = valid_post_data
        invalid_post_data['api_key'] = '123'
        resp = self.client.post('/review-apps/', invalid_post_data)
        assert resp.status_code == 400
        assert resp.status_text == 'Bad Request'
        assert resp.json() == {'api_key': ['Improperly formatted API KEY format']}
