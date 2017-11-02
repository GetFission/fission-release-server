from django.db import models
from django_extensions.db import models as dj_models


class Branch(dj_models.TimeStampedModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    project = models.ForeignKey(
        'projects.Project',
        null=True,
        blank=True,
        related_name='branches'
    )


class Commit(dj_models.TimeStampedModel):
    branch = models.ForeignKey(
        'review_apps.Branch',
        null=True,
        blank=True,
        related_name='commits'
    )
    commit_hash = models.CharField(
        unique=True,
        max_length=255,
        blank=True,
        null=True
    )


class ReviewAppBuild(dj_models.TimeStampedModel):
    commit = models.ForeignKey(
        'review_apps.Commit',
        null=True,
        related_name='builds'
    )
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
        ('local', 'local'),
        ('N/A', 'N/A'),
    )
    ci = models.CharField(max_length=50, choices=CI_CHOICES)

    app_version = models.CharField(max_length=50, blank=True, null=True)

    build_url = models.CharField(max_length=255, blank=True, null=True)
    ci_job_id = models.CharField(max_length=50, blank=True, null=True)
    pull_request_number = models.CharField(
        max_length=255, blank=True, null=True
    )
