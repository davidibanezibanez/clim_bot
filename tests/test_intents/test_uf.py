from unittest.mock import patch
from intents.uf import get_uf

def test_get_uf_success():
    mock_data = {"uf": {"valor": 35982.42}}
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_data
        result = get_uf()
        assert "35982.42" in result

def test_get_uf_connection_error():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = Exception("Error de conexión")
        result = get_uf()
        assert result == "Error al obtener el valor de la UF."