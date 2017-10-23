from rest_framework import serializers

from review_apps import models


class ReviewAppBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReviewAppBuild
        fields = (
            'id',
            'platform',
            'ci',
            'app_version',
            'branch_name',
            'commit_hash',
            'ci_job_id',
            'pull_request_number'
        )
