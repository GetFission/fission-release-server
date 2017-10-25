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
        # TODO: log uncaught errors
        raise serializers.ValidationError('Error looking up API KEY')
    raise serializers.ValidationError('Invalid API KEY')


class ReviewAppBuildSerializer(serializers.ModelSerializer):
    api_key = serializers.CharField(write_only=True, max_length=255,  validators=[validate_api_key])
    created = serializers.DateTimeField(read_only=True)
    class Meta:
        model = models.ReviewAppBuild
        fields = (
            'api_key',
            'app_version',
            'branch_name',
            'build_url',
            'ci',
            'ci_job_id',
            'commit_hash',
            'created',
            'id',
            'project',
            'platform',
            'pull_request_number'
        )

    def create(self, validated_data):
        api_key = validated_data.pop('api_key')
        project = project_models.Project.objects.get(api_key=api_key)
        validated_data['project'] = project
        build = models.ReviewAppBuild.objects.create(**validated_data)
        return build

