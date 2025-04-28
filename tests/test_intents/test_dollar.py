import pytest
from unittest.mock import patch
from intents.dollar import get_dollar

def test_get_dollar_success():
    mock_data = {"dolar": {"valor": 956.42}}
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_data
        result = get_dollar()
        assert "956.42" in result

def test_get_dollar_api_down():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 500
        result = get_dollar()
        assert "No pude obtener" in result

def test_get_dollar_invalid_response():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {}
        result = get_dollar()
        assert "No pude obtener" in result