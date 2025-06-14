import requests

url = "https://jsonplaceholder.typicode.com/posts"
new_post = {
    "title": "Mi nuevo post",
    "body": "Contenido del post",
    "userId": 6
}

response = requests.post(url, json=new_post)
print(response.json())
