from rest_framework import serializers

from releases import models as releases_models


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
            'project': {'required': True}
        }

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
