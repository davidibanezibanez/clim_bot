import requests

def get_dollar():
    url = "https://mindicador.cl/api"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'dolar' in data and 'valor' in data['dolar']:
                return f"El valor actual del dólar es ${data['dolar']['valor']} CLP."
        return "No pude obtener el valor del dólar en este momento."
    except Exception:
        return "Error al conectar con el servicio."