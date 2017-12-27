from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class ExampleView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)