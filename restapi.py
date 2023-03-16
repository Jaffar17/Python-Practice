import requests

# GET
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.json())
print(response.status_code)

# POST
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {'userId': 1,  'title': 'Jaffar POST', 'completed': True}
response = requests.post(api_url, json=todo)
print(response.json())
print(response.status_code)

# PUT
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())
print(response.status_code)

todo = {'userId': 1, 'title': 'Jaffar PUT', 'completed': True}
response = requests.put(api_url, json=todo)
print(response.json())
print(response.status_code)

# PATCH
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())
print(response.status_code)

todo = {'title': 'Jaffar PATCH'}
response = requests.patch(api_url, json=todo)
print(response.json())
print(response.status_code)

# DELETE
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(response.json())
print(response.status_code)


