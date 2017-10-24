import uuid

from django.db import models
from django_extensions.db import models as dj_models


class ReviewAppBuild(dj_models.TimeStampedModel):
    project = models.ForeignKey('projects.Project', null=True)
    api_key = models.UUIDField(blank=True, null=True)

    PLATFORM_CHOICES = (
        ('darwin', 'darwin'),
        ('linux32', 'linux32'),
        ('linux64', 'linux64'),
        ('win32', 'win32'),
        ('win64', 'win64')
    )
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)

    CI_CHOICES = (
        ('appveyor', 'appveyor'),
        ('travis', 'travis'),
        ('teamcity', 'teamcity'),
        ('jenkins', 'jenkins'),
    )
    ci = models.CharField(max_length=50, choices=CI_CHOICES)

    app_version = models.CharField(max_length=50, blank=True, null=True)
    branch_name = models.CharField(max_length=255, blank=True, null=True)
    commit_hash = models.CharField(max_length=255, blank=True, null=True)

    build_url = models.CharField(max_length=50, blank=True, null=True)
    ci_job_id = models.CharField(max_length=50, blank=True, null=True)
    pull_request_number = models.CharField(
        max_length=255, blank=True, null=True
    )
