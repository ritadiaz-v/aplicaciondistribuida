import requests

url = "http://127.0.0.1:5000/crear_carpeta"

datos = {
    "ruta_base": "D:/MisCarpetas",
    "subcarpetas": ["2025", "proyecto1"]
}

response = requests.post(url, json=datos)

print("Respuesta:", response.json())
