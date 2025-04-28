import requests
import os

def get_news():
    api_key = os.getenv("GNEWS_API_KEY")

    url = f"https://gnews.io/api/v4/top-headlines?lang=es&token={api_key}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])

            if not articles:
                return "No se encontraron noticias para mostrar."

            news_list = [f"- {article['title']}" for article in articles[:10]]
            return "Aquí están las noticias principales:\n" + "\n".join(news_list)
        elif response.status_code == 401:
            return "Error de autenticación: verifica que tu clave de API sea válida."
        else:
            return "No pude obtener las noticias en este momento."
    except Exception:
        return "Ocurrió un error al obtener las noticias."
-
-
-
test_news.py:
-
-
-
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
