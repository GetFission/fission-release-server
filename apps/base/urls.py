from django.conf.urls import url

from base import views as base_views

urlpatterns = [
    url(r'^collect-email/$',
        base_views.collect_email,
        name='collect_email'),
    url(r'',
        base_views.ProtectedDataView.as_view(),
        name='protected_data'),
]
