from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from projects import models, serializers


class ProjectCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectCreateSerializer


class ProjectListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProjectCreateSerializer

    def get_queryset(self):
        return models.Project.objects.filter(created_by=self.request.user)
