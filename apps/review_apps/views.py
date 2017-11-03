from rest_framework import generics

from review_apps import models, serializers


class ReviewAppBuildCreateView(generics.CreateAPIView):
    authentication_classes = ()  # set to empty to avoid CSRF
    queryset = models.ReviewAppBuild.objects.all()
    serializer_class = serializers.ReviewAppBuildCreateSerializer


class ReviewAppBuildListView(generics.ListAPIView):
    serializer_class = serializers.BranchSerializer

    def get_queryset(self):
        project_slug = self.kwargs['project_slug']
        return models.Branch.objects.filter(project__slug=project_slug)


class ReviewAppBuildDetail(generics.RetrieveUpdateAPIView):
    queryset = models.ReviewAppBuild.objects.all()
    serializer_class = serializers.ReviewAppBuildSerializer

