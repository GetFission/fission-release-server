from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from releases import models, serializers


class ReleaseCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.Release.objects.all()
    serializer_class = serializers.ReleaseCreateSerializer


class ReleaseListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ReleaseListSerializer

    def get_queryset(self):
        return (
            models.Release.objects
            # .filter(project__slug=self.kwargs['project_slug'])
            .order_by('created')
        )

class ReleaseRuleMembersListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ReleaseRuleMemberSerializer

    def get_queryset(self):
        release_rule = models.ReleaseRule.objects.get(id=self.kwargs['rule_id'])
        release_rule.generate_members()
        return (
            models.ReleaseMember.objects
            .filter(release_rule_id=self.kwargs['rule_id'])
            .order_by('created')
        )
