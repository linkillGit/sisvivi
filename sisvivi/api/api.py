#---> Funciones de fecha y tiempo
from datetime import datetime

#---> Consultas a HTTPS
import requests


async def get_repo_updated_at(owner: str, repo: str) -> str:
    """ DESCRIPCIÓN
    
    Obtiene la fecha de la última actualización de un repositorio de GitHub y la devuelve formateada como una cadena.

    Argumentos:
        owner (str): Nombre del propietario del repositorio.
        repo (str): Nombre del repositorio.

    Returns:
        str: Cadena formateada con la fecha de la última actualización.
    """

    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}")
    response.raise_for_status()  # Levantar una excepción si la solicitud falla
    data = response.json()

    try:
        updated_at = datetime.fromisoformat(data["updated_at"][:-1])  # Eliminamos la 'Z'
        formatted_date = f"Repositorio actualizado el {updated_at.strftime('%d/%m/%Y a las %H:%M:%S')}"
        return formatted_date
    except ValueError:
        print("Error al parsear la fecha. Valor devuelto: None")
        return None