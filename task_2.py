import requests

# Параметры запроса
params = {'userId': 1}

# Отправляем GET-запрос с параметрами
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

# Проверяем статус-код
print(response.status_code)

# Выводим данные
print(response.json())
