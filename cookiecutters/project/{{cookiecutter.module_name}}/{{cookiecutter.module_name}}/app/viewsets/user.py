from django.contrib.auth.models import User
from rest_framework import viewsets

from {{cookiecutter.module_name}}.app.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
