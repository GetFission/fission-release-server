from rest_framework import serializers

from projects import models as project_models


class ProjectCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = project_models.Project
        fields = (
            'name',
            'rms_url',
            'slug'
        )

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
