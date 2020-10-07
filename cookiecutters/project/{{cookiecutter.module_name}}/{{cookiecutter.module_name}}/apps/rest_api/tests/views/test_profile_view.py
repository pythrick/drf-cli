import pytest


@pytest.mark.django_db
def test_unauthorized_request_on_route_me(api_client):
    response = api_client.get("/api/v1/me")
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request(api_client_with_credentials):
    response = api_client_with_credentials.get("/api/v1/me")
    assert response.status_code == 200
