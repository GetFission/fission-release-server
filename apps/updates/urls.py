from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from updates import views


urlpatterns = [
    url(r'.*', views.update_view_func),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
