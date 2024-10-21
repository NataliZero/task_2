import requests

params = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

print(response.status_code)
print(response.json())
