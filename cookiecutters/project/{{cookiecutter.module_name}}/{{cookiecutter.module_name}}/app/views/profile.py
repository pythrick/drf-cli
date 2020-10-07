from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from {{cookiecutter.module_name}}.app.serializers import ProfileSerializer


class MeProfileView(APIView):
    """
    View to retrieve current profile in the system.

    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return the current user
        """
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
