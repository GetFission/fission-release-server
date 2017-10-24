from rest_framework import serializers
from django.core.exceptions import ValidationError

from projects import models as project_models
from review_apps import models


def validate_api_key(api_key):
    try:
        if project_models.Project.objects.filter(api_key=api_key).count() == 1:
            return api_key
    except ValidationError:
        raise serializers.ValidationError('Improperly formatted API KEY format')
    except Exception as e:
        print('Failed to find api key', e)
        raise serializers.ValidationError('Invalid API KEY')


class ReviewAppBuildSerializer(serializers.ModelSerializer):
    api_key = serializers.CharField(max_length=255,  validators=[validate_api_key])
    class Meta:
        model = models.ReviewAppBuild
        fields = (
            'id',
            'project',
            'api_key',
            'platform',
            'ci',
            'app_version',
            'branch_name',
            'commit_hash',
            'ci_job_id',
            'pull_request_number'
        )

    extra_kwargs = {"api_key": {"error_messages": {"required": "Valid api_key required"}}}

    def create(self, validated_data):
        api_key = validated_data.pop('api_key')
        project = project_models.Project.objects.get(api_key=api_key)
        validated_data['project'] = project
        build = models.ReviewAppBuild.objects.create(**validated_data)
        return build

