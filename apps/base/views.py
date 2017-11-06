import os

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View
from knox.auth import TokenAuthentication
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import logging

logger = logging.getLogger('raven')


class IndexView(View):
    """Render main page."""

    def get(self, request):
        """Return html for main application page."""
        abspath = open(os.path.join(settings.BASE_DIR, 'static/index.html'), 'r')
        logger.error('There was some crazy error', exc_info=True, extra={
            # Optionally pass a request and we'll grab any information we can
            'request': request,
        })
        return HttpResponse(content=abspath.read())


class ProtectedDataView(GenericAPIView):
    """Return protected data main page."""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """Process GET request and return protected data."""

        data = {
            'data': 'THIS IS THE PROTECTED STRING FROM SERVER',
        }

        return Response(data, status=status.HTTP_200_OK)
