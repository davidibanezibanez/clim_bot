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
