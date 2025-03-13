from app.settings import Pax8Settings

def test_pax8_settings_initialization():
    settings = Pax8Settings(
        client_id="test_client_id",
        client_secret="test_client_secret",
        audience="test_audience",
        grant_type="client_credentials",
        base_url="https://api.test.com"
    )
    assert settings.client_id == "test_client_id"
    assert settings.client_secret == "test_client_secret"
    assert settings.audience == "test_audience"
    assert settings.grant_type == "client_credentials"
    assert settings.base_url == "https://api.test.com"
