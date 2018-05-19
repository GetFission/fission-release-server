from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from releases import views


urlpatterns = [
    url(r'^create/$', views.ReleaseCreateView.as_view()),
    url(r'^list/members/(?P<rule_id>[\w-]+)/$', views.ReleaseRuleMembersListView.as_view()),
    url(r'^list/(?P<project_slug>[\w-]+)/$', views.ReleaseListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
