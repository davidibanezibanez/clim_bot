import requests
import os

def get_weather(city, country=None):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not country:
        return "Por favor, especifica el país para obtener el clima."
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric&lang=es"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"El clima en {city}, {country} es {weather} con una temperatura de {temp}°C."
    elif response.status_code == 404:
        return f"No encontré información para la ciudad '{city}' en el país '{country}'. Por favor, verifica los datos."
    else:
        return "Ocurrió un error al obtener el clima. Inténtalo más tarde."