from django.test import override_settings
from rest_framework.test import APITestCase

from projects import models as project_models
from review_apps import models as review_app_models


@override_settings()
class ReviewAppsTestCase(APITestCase):
    def setUp(self):
        self.project = project_models.Project.objects.create(name='Test Project')

    def test_post_build_ping(self):
        valid_post_data = { "ci": "appveyor",
                 "platform": "win32",
                 "branch": "master",
                 "build_url": "example.com/foo/123",
                 "commit_hash": "123456",
                 "ci_job_id": "22",
                 "app_version": "1.4.5",
                 "pull_request_number": "33",
                 "api_key": str(self.project.api_key)
        }
        resp = self.client.post('/api/v1/review-apps/ping/', valid_post_data)
        assert resp.status_code == 201
        assert resp.status_text == 'Created'

        res = resp.json()
        res.pop('id')  # remove id
        res.pop('created')  # remove created time stamp
        commit_id = res.pop('commit')
        commit = review_app_models.Commit.objects.get(pk=commit_id)
        assert commit is not None
        assert commit.branch.name == valid_post_data['branch']

        assert res['app_version'] == valid_post_data['app_version']
        assert res['build_url'] == valid_post_data['build_url']
        assert res['ci_job_id'] == valid_post_data['ci_job_id']
        assert res['platform'] == valid_post_data['platform']
        assert res['pull_request_number'] == valid_post_data['pull_request_number']


        invalid_post_data = valid_post_data
        invalid_post_data.pop('api_key')
        resp = self.client.post('/api/v1/review-apps/ping/', invalid_post_data)
        assert resp.status_code == 400
        assert resp.status_text == 'Bad Request'
        assert resp.json() == {'api_key': ['This field is required.']}

        invalid_post_data = valid_post_data
        invalid_post_data['api_key'] = '123'
        resp = self.client.post('/api/v1/review-apps/ping/', invalid_post_data)
        assert resp.status_code == 400
        assert resp.status_text == 'Bad Request'
        assert resp.json() == {'api_key': ['Improperly formatted API KEY format']}


    # TODO: Finish implementing test
    # def test_get_review_apps_list(self):
    #     project = project_models.Project.objects.create(name='Foo')
    #     import pdb; pdb.set_trace()
    #     branches = [
    #         review_app_models.Branch.objects.create(name=name)
    #         for name in ['master', 'hotfix']
    #     ]
    #     commits = [
    #         review_app_models.Commit.objects.create(branch=branch)
    #         for branch in branches
    #     ]
    #     travis_linux_builds = [
    #         review_app_models.ReviewAppBuild.objects.create(
    #             commit=commit,
    #             ci='travis',
    #             platform='linux'
    #         )
    #         for commit in commits
    #     ]
    #     appveyor_win_builds = [
    #         review_app_models.ReviewAppBuild.objects.create(
    #             commit=commit,
    #             ci='appveyor',
    #             platform='win32'
    #         )
    #         for commit in commits
    #     ]
    #
    #     print('/api/v1/review-apps/{}/'.format(project.slug))
    #     resp = self.client.get('/api/v1/review-apps/{}/'.format(project.slug))
    #     assert resp.status_code == 200
