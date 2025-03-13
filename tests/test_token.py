import pytest
from unittest.mock import patch, MagicMock
from app.manager import Pax8Manager
from app.settings import Pax8Settings

@pytest.fixture
def pax8_manager():
    settings = Pax8Settings(
        client_id="test_client_id",
        client_secret="test_client_secret",
        audience="test_audience",
        grant_type="client_credentials",
        base_url="https://api.test.com"
    )
    return Pax8Manager(settings)

@patch("requests.post")
def test_get_access_token(mock_post, pax8_manager):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "access_token": "test_token",
        "expires_in": 3600,
        "token_type": "Bearer"
    }
    mock_post.return_value = mock_response

    response = pax8_manager.get_access_token()
    assert response.is_success
    assert response.content.access_token == "test_token"
    assert response.content.expires_in == 3600
    assert response.content.token_type == "Bearer"
