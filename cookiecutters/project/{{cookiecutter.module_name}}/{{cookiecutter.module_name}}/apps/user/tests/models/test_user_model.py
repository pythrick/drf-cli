import uuid

import pytest


@pytest.mark.django_db
class TestUserModel:
    def test_pk(self, user):
        assert isinstance(
            user.pk, uuid.UUID
        ), f"The {user.__class__.__name__} pk should be an UUID field."

    def test_string(self, user):
        assert str(user) == f"{user.__class__.__name__}<{user.pk}>"

    def test_repr(self, user):
        assert str(user) == f"{user.__class__.__name__}<{user.pk}>"