import requests

def get_uf():
    url = "https://mindicador.cl/api"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"El valor actual de la UF es ${data.get('uf', {}).get('valor', 'N/A')} CLP."
        return "No pude obtener el valor de la UF en este momento."
    except requests.exceptions.ConnectionError:
        return "Error de conexión al servicio."
    except Exception:
        return "Error al obtener el valor de la UF."