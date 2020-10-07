import pytest

from ...serializers import ProfileSerializer


@pytest.fixture
def serialized_user(user):
    return ProfileSerializer(user)


@pytest.mark.django_db
def test_serialize_profile(serialized_user):
    assert list(serialized_user.data.keys()) == ["id", "email", "name"]
