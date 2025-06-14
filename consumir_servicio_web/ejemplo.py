import requests

# Paso 1: Definir la URL
url = "https://jsonplaceholder.typicode.com/posts"

# Paso 2: Hacer la solicitud GET
response = requests.get(url)

# Paso 3: Verificar si la solicitud fue exitosa
if response.status_code == 200:
    posts = response.json()  # Convertir la respuesta en JSON
    for post in posts[:7]:  # Mostrar solo los primeros 5
        print(f"ID: {post['id']} - Título: {post['title']}")
else:
    print("Error al consumir el servicio:", response.status_code)
