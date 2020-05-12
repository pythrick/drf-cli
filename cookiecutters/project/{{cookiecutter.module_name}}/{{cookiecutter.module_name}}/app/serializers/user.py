# Serializers define the API representation.
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "email",
            "name",
            "last_login",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("id", "last_login", "created_at", "updated_at")
