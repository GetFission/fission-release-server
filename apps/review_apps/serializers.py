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


class ReviewAppBuildCreateSerializer(serializers.ModelSerializer):
    api_key = serializers.CharField(write_only=True, max_length=255,  validators=[validate_api_key])
    branch = serializers.CharField(write_only=True, max_length=255, required=True)
    commit_hash = serializers.CharField(write_only=True, max_length=255, required=True)

    class Meta:
        model = models.ReviewAppBuild
        fields = (
            'api_key',
            'app_version',
            'branch',
            'build_url',
            'ci',
            'ci_job_id',
            'commit',
            'commit_hash',
            'created',
            'id',
            'platform',
            'pull_request_number'
        )

    def create(self, validated_data):
        api_key = validated_data.pop('api_key')
        project = project_models.Project.objects.get(api_key=api_key)

        branch, _ = models.Branch.objects.get_or_create(
            project=project,
            name=validated_data.pop('branch')
        )

        commit, _ = models.Commit.objects.get_or_create(
            branch=branch,
            commit_hash=validated_data.pop('commit_hash')
        )

        validated_data['commit'] = commit
        build = models.ReviewAppBuild.objects.create(**validated_data)
        return build



class ReviewAppBuildSerializer(serializers.ModelSerializer):
    api_key = serializers.CharField(
        write_only=True, max_length=255,  validators=[validate_api_key]
    )
    created = serializers.DateTimeField(read_only=True)
    # project_slug = serializers.ReadOnlyField(source='project.slug')
    class Meta:
        model = models.ReviewAppBuild
        fields = (
            'api_key',
            'app_version',
            'build_url',
            'ci',
            'ci_job_id',
            'commit',
            'created',
            'id',
            'platform',
            'pull_request_number'
        )


class CommitSerializer(serializers.ModelSerializer):
    builds = ReviewAppBuildSerializer(many=True, read_only=True)
    class Meta:
        model = models.Commit
        fields = ('commit_hash', 'builds')


class BranchSerializer(serializers.ModelSerializer):
    commits = CommitSerializer(many=True, read_only=True)
    class Meta:
        model = models.Branch
        fields = ('project', 'name', 'commits')


# class ReviewAppBuildListSerializer(serializers.ModelSerializer):
#     api_key = serializers.CharField(
#         write_only=True, max_length=255,  validators=[validate_api_key]
#     )
#     created = serializers.DateTimeField(read_only=True)
#     project_slug = serializers.ReadOnlyField(source='project.slug')
#     class Meta:
#         model = models.ReviewAppBuild
#         fields = (
#             'api_key',
#             'app_version',
#             'branch_name',
#             'build_url',
#             'ci',
#             'ci_job_id',
#             'commit_hash',
#             'created',
#             'id',
#             'project',
#             'project_slug',
#             'platform',
#             'pull_request_number'
#         )
