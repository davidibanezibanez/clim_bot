import discord
import os
from dotenv import load_dotenv
import re
import requests
from nlp.processor import get_intent
from intents.weather import get_weather
from intents.uf import get_uf
from intents.dollar import get_dollar
from intents.news import get_news

import sys

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OPENCAGE_API_KEY = os.getenv("OPENCAGE_API_KEY")

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

def get_country_code(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]["cca2"].upper()
    return None

def get_country_from_city(city):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={OPENCAGE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            components = data["results"][0]["components"]
            country_code = components.get("country_code", "").upper()
            return country_code
    return None

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    intent = get_intent(message.content)
    response = ""

    if intent == "weather":
        match = re.search(r"(en|de)\s+([\w\s]+)(,\s*([\w\s]+))?", message.content, re.IGNORECASE)
        if match:
            city = match.group(2).strip().capitalize()
            country_name = match.group(4)
            
            if country_name:
                country_name = country_name.strip().capitalize()
                country_code = get_country_code(country_name)
                if not country_code:
                    response = f"No pude encontrar el país '{country_name}'. Por favor, verifica el nombre."
                else:
                    response = get_weather(city, country_code)
            else:
                country_code = get_country_from_city(city)
                if not country_code:
                    response = f"No pude determinar el país para la ciudad '{city}'. Por favor, especifícalo."
                else:
                    response = get_weather(city, country_code)
        else:
            response = "No entendí la ciudad que mencionaste. Por favor, intenta de nuevo."
    elif intent == "uf":
        response = get_uf()
    elif intent == "dollar":
        response = get_dollar()
    elif intent == "news":
        response = get_news()
    else:
        response = "Lo siento, no entendí tu solicitud."

    await message.channel.send(response)

def setup_hook():
    """Setup hook for discord.py"""
    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

if 'pytest' in sys.modules:
    import asyncio
    try:
        loop = asyncio.get_event_loop()
        if not client.is_closed():
            loop.run_until_complete(client.close())
    except RuntimeError:
        pass

if __name__ == "__main__":
    client.run(TOKEN)
