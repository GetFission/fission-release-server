from rest_framework import generics

from review_apps import models, serializers


class ReviewAppBuildCreateView(generics.CreateAPIView):
    queryset = models.ReviewAppBuild.objects.all()
    serializer_class = serializers.ReviewAppBuildCreateSerializer


class ReviewAppBuildListView(generics.ListAPIView):
    queryset = models.ReviewAppBuild.objects.all()
    serializer_class = serializers.ReviewAppBuildListSerializer

    def get_queryset(self):
        project_slug = self.kwargs['project_slug']
        return models.ReviewAppBuild.objects.filter(project__slug=project_slug)


class ReviewAppBuildDetail(generics.RetrieveUpdateAPIView):
    queryset = models.ReviewAppBuild.objects.all()
    serializer_class = serializers.ReviewAppBuildListSerializer

