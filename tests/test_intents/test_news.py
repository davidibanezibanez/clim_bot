import os
from unittest.mock import patch
from intents.news import get_news

def test_get_news_success(monkeypatch):
    monkeypatch.setenv("GNEWS_API_KEY", "fake_key")
    mock_data = {
        "articles": [
            {"title": "Terremoto en Chile"},
            {"title": "Nueva constitución"}
        ]
    }
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_data
        result = get_news()
        assert "Terremoto" in result
        assert "constitución" in result

def test_get_news_empty_response():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"articles": []}
        result = get_news()
        assert "No se encontraron" in result
