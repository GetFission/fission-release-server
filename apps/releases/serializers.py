from rest_framework import serializers

from releases import models as releases_models


class ReleaseCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    # slug = serializers.SlugField(read_only=True)

    class Meta:
        model = releases_models.Release
        fields = (
            'name',
            'version',
            'darwin_artifact',
            'windows_artifact',
            'project'
        )

    def create(self, validated_data):
        import pdb; pdb.set_trace()
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
