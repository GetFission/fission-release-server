from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from projects import views


urlpatterns = [
    url(r'^create/$', views.ProjectCreateView.as_view()),
    url(r'^list/$', views.ProjectListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
