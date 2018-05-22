from rest_framework import serializers

from releases import models as releases_models
from projects import models as project_models


class ReleaseCreateSerializer(serializers.ModelSerializer):
    project_slug = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = releases_models.Release
        fields = (
            'name',
            'version',
            'darwin_zip',
            'darwin_zip_sha512',
            'nsis_exe',
            'nsis_exe_sha512',
            'project',
            'project_slug'
        )
        extra_kwargs = {
            'version': {'required': True},
        }

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        if 'project_slug' in validated_data:
            slug = validated_data.pop('project_slug')
            project = project_models.Project.objects.get(slug=slug)
            validated_data['project'] = project
        return super().create(validated_data)


    def validate(self, attrs):
        if 'project' not in attrs and 'project_slug' not in attrs:
            raise serializers.ValidationError('project is a required field')
        return super().validate(attrs)


class ReleaseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = releases_models.Release
        fields = (
            'id',
            'created',
            'name',
            'version',
            'darwin_zip',
            'nsis_exe',
            'project',
        )


class ReleaseRuleMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = releases_models.ReleaseMember
        fields = '__all__'
