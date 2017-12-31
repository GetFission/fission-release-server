from rest_framework import serializers

from projects import models as project_models


class ProjectCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = project_models.Project
        fields = (
            'name',
            'rms_url'
        )
