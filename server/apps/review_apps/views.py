from rest_framework import generics

from review_apps import models, serializers


class ReviewAppBuildList(generics.ListCreateAPIView):
    queryset = models.ReviewAppBuild.objects.all()
    serializer_class = serializers.ReviewAppBuildSerializer


class ReviewAppBuildDetail(generics.RetrieveUpdateAPIView):
    queryset = models.ReviewAppBuild.objects.all()
    serializer_class = serializers.ReviewAppBuildSerializer