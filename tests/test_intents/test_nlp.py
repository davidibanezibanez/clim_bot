import pytest
from nlp.processor import normalize_text, get_intent

def test_normalize_text():
    assert normalize_text("ClImÁ") == "clima"
    assert normalize_text("¿Dólar?") == "dolar"
    assert normalize_text("AÑO 2023") == "ano 2023"
    assert normalize_text("Unidad de Fomento") == "unidad de fomento"

@pytest.mark.parametrize("input_text, expected", [
    ("¿Cómo está el clima?", "weather"),
    ("Dime el tiempo en Santiago", "weather"),
    ("valor UF", "uf"),
    ("unidad de fomento hoy", "uf"),
    ("cotización dólar", "dollar"),
    ("precio del usd", "dollar"),
    ("últimas noticias", "news"),
    ("Qué novedades hay", "news"),
    ("hola bot", "unknown"),
])
def test_get_intent(input_text, expected):
    assert get_intent(input_text) == expected