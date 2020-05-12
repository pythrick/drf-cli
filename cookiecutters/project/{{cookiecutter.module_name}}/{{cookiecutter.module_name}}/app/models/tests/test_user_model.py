import uuid

import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestUserModel:
    @pytest.fixture
    def user(self):
        return mixer.blend("app.User")


    def test_pk(self, user):
        assert isinstance(
            user.pk, uuid.UUID
        ), f"The {user.__class__.__name__} pk should be an UUID field."

    def test_string(self, user):
        assert str(user) == f"{user.name}"
