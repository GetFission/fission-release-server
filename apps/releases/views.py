from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from releases import models, serializers


class ReleaseCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.Release.objects.all()
    serializer_class = serializers.ReleaseCreateSerializer


class ReleaseListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ReleaseCreateSerializer

    def get_queryset(self):
        return (
            models.Release.objects
            .order_by('created')
        )
