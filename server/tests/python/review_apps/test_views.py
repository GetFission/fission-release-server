from django.test import override_settings
from rest_framework.test import APITestCase

from projects import models as project_models
from review_apps import models as review_app_models


@override_settings()
class ReviewAppsTestCase(APITestCase):
    def setUp(self):
        self.project = project_models.Project.objects.create(name='Test Project')

    def test_post_build_ping(self):
        data = { "ci": "appveyor",
                 "platform": "win32",
                 "branch_name": "master",
                 "commit_hash": "123456",
                 "ci_job_id": "22",
                 "app_version": "1.4.5",
                 "pull_request_number": "33",
                 "api_key": str(self.project.api_key)
        }
        resp = self.client.post('/review-apps/', data)
        res = resp.json()
        res.pop('id')  # remove id

        expected = {'project': self.project.id, **data}
        expected.pop('api_key')
        assert expected == res
        # import pdb; pdb.set_trace()
