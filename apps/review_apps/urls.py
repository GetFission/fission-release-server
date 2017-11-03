from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from review_apps import views


urlpatterns = [
    url(r'^(?P<project_slug>.*)/(?P<pk>[0-9]+)/$', views.ReviewAppBuildDetail.as_view()),
    url(r'^ping/$', views.ReviewAppBuildCreateView.as_view()),
    url(r'^(?P<project_slug>.*)/$', views.ReviewAppBuildListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
