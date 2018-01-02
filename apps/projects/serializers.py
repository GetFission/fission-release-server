from rest_framework import serializers

from projects import models as project_models


class ProjectCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = project_models.Project
        fields = (
            'name',
            'rms_url',
            'slug'
        )

    def create(self, validated_data):
        validated_data['created_by'] = self.request.user
        return super().create(validated_data)
