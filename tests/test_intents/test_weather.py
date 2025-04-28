import os
from unittest.mock import patch
from intents.weather import get_weather

def test_get_weather_success(monkeypatch):
    monkeypatch.setenv("OPENWEATHER_API_KEY", "fake_key")
    mock_data = {
        "weather": [{"description": "cielo claro"}],
        "main": {"temp": 22.3}
    }
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_data
        result = get_weather("Santiago", "CL")
        assert "cielo claro" in result
        assert "22.3" in result

def test_get_weather_city_not_found():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        result = get_weather("UnknownCity", "XX")
        assert "No encontré información" in result