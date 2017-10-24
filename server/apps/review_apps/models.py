from django.db import models
from django_extensions.db import models as dj_models


class ReviewAppBuild(dj_models.TimeStampedModel):
    PLATFORM_CHOICES = (
        ('darwin', 'darwin'),
        ('linux32', 'linux32'),
        ('linux64', 'linux64'),
        ('win32', 'win32'),
        ('win64', 'win64')
    )
    CI_CHOICES = (
        ('appveyor', 'appveyor'),
        ('travis', 'travis'),
        ('teamcity', 'teamcity'),
        ('jenkins', 'jenkins'),
    )

    # project = models.ForeignKey('projects.project')

    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    ci = models.CharField(max_length=50, choices=CI_CHOICES)

    app_version = models.CharField(max_length=50, blank=True, null=True)
    branch_name = models.CharField(max_length=255, blank=True, null=True)
    commit_hash = models.CharField(max_length=255, blank=True, null=True)

    ci_job_id = models.CharField(max_length=50, blank=True, null=True)
    pull_request_number = models.CharField(
        max_length=255, blank=True, null=True
    )
