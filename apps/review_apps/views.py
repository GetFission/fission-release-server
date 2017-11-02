from rest_framework import generics

from review_apps import models, serializers


class ReviewAppBuildCreateView(generics.CreateAPIView):
    queryset = models.ReviewAppBuild.objects.all()
    serializer_class = serializers.ReviewAppBuildCreateSerializer


class ReviewAppBuildListView(generics.ListAPIView):
    # queryset = models.ReviewAppBuild.objects.all()
    # queryset = models.Branch.objects.all()
    serializer_class = serializers.BranchSerializer

    def get_queryset(self):
        project_slug = self.kwargs['project_slug']
        return models.Branch.objects.filter(project__slug=project_slug)


class ReviewAppBuildDetail(generics.RetrieveUpdateAPIView):
    queryset = models.ReviewAppBuild.objects.all()
    serializer_class = serializers.ReviewAppBuildSerializer


"""
/review-apps/<project-slug>/<branch>/
{'builds': [build 1...N]}

/review-apps/<project-slug>/<get-branches>/
{'branches': [branch 1....N]}

/review-apps/<project-slug>/?page=2
{'branches': 'master': [build 1...N], 'hotfix': [build 1.... N]}

/review-apps/<project-slug>/build-id/detail/
{...build info}

"""

# class CommitsListView(generics.ListAPIView):
#     # queryset = models.ReviewAppBuild.objects.all()
#     serializer_class = serializers.ReviewAppBuildListSerializer
#
#     def get_queryset(self):
#         project_slug = self.kwargs['project_slug']
#         commits = (
#             models.Commit.objects
#             .filter(project__slug=project_slug)
#             .order_by('-created')
#             .distinct('branch')
#             .limit(10)
#         )
#         branches = [commit.branch for commit in commits]
#
#         data = {}
#         for branch in branches:
#             data[branch] = models.Commit.objects.filter(
#                 branch=branch,
#                 project__slug=project_slug
#             )
#         return data
#

