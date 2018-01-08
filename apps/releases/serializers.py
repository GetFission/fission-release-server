from rest_framework import serializers

from releases import models as releases_models
from projects import models as project_models


class ReleaseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = releases_models.Release
        fields = (
            'name',
            'version',
            'darwin_artifact',
            'windows_artifact',
            'project'
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


    def validate(self, data):
        if 'project' not in data and 'project_slug' not in data:
            raise serializers.ValidationError('project is a required field')
        return super().validate(data)

        