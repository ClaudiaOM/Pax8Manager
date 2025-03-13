import pytest
from unittest.mock import patch, MagicMock
from app.manager import Pax8Manager
from app.settings import Pax8Settings
from app.models.response import ResponseModel, CompanyResponse

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

@patch("requests.get")
def test_get_company(mock_get, pax8_manager):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": "company123",
        "name": "Test Company"
    }
    mock_get.return_value = mock_response

    response = pax8_manager.get_company("company123")
    assert response.is_success
    assert response.content["id"] == "company123"
    assert response.content["name"] == "Test Company"
