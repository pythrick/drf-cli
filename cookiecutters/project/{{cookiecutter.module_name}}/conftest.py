import pytest
from faker import Faker
from mixer.backend.django import mixer


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def api_client_with_credentials(user, api_client):
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)


@pytest.fixture
def fake():
    return Faker()


@pytest.fixture
def user():
    return mixer.blend("user.User")
