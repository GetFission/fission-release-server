from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView, RedirectView

from base import views as base_views

from auth0authorization import views as auth_views

urlpatterns = [
    url(r'^profile/$', auth_views.ProfileView.as_view()),
    url(r'^api/v1/review-apps/', include('review_apps.urls', namespace='review-apps')),
    url(r'^api/v1/getdata/', include('base.urls', namespace='base')),
    url(r'^api/v1/rules/', include('rules.urls', namespace='rules')),
    url(r'^lifa-tree/', admin.site.urls),

    url(r'^$',
        cache_page(settings.PAGE_CACHE_SECONDS)(base_views.IndexView.as_view()),
        name='index'
    ),
]
