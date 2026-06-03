import pytest

from utils.api_client import ApiClient
from utils.api_assertions import (
    assert_status_code,
    assert_response_key
)
from data.api_payloads import CREATE_POST_PAYLOAD
from utils.config import Config



@pytest.fixture
def api_client():
    return ApiClient(
        Config.API_BASE_URL
    )


@pytest.mark.api
@pytest.mark.smoke
def test_get_users(api_client):
    response = api_client.get("/users")
    body = response.json()

    assert_status_code(response, 200)

    assert len(body) > 0

    assert_response_key(body[0], "email")


@pytest.mark.api
@pytest.mark.regression
def test_create_post(api_client):
    response = api_client.post("/posts", CREATE_POST_PAYLOAD)
    body = response.json()

    assert_status_code(response, 201)
    assert body["title"] == CREATE_POST_PAYLOAD["title"]
    assert body["body"] == CREATE_POST_PAYLOAD["body"]
    assert body["userId"] == CREATE_POST_PAYLOAD["userId"]
    assert body["id"] is not None


@pytest.mark.api
@pytest.mark.regression
def test_delete_post(api_client):
    response = api_client.delete("/posts/1")

    assert_status_code(response, 200)