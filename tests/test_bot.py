import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from bot import client, get_country_code, get_country_from_city

def test_get_country_code_success():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"cca2": "CL"}]
        assert get_country_code("Chile") == "CL"

@pytest.mark.asyncio
async def test_bot_weather_intent():
    message = AsyncMock()
    message.content = "Clima en París, Francia"
    message.author = MagicMock()
    message.author.bot = False

    with patch('intents.weather.get_weather') as mock_weather:
        mock_weather.return_value = "El clima en París, FR es cielo claro con una temperatura de 13.13°C."
        await client.on_message(message)
        message.channel.send.assert_called_once()

@pytest.mark.asyncio
async def test_bot_unknown_intent():
    message = AsyncMock()
    message.content = "mensaje sin sentido"
    message.author.bot = False

    with patch('nlp.processor.get_intent') as mock_intent:
        mock_intent.return_value = "unknown"
        await client.on_message(message)
        message.channel.send.assert_called_with("Lo siento, no entendí tu solicitud.")

@pytest.fixture
def mock_discord_client():
    with patch('discord.Client') as mock_client:
        yield mock_client