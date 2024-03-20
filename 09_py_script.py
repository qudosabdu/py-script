# Working with APIs

import requests
import json

# Make an API request
response = requests.get('https://jsonplaceholder.typicode.com/todos/3')

# check if the request was successful
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
    

todos = json.loads(response.text) #converts the JSON string into a Python dictionary

# print the data from the API
# print(todos)

# CREATE a new JSON file and write the data to it
todos_data = {
    "userId": '100',
    "id": '100',
    "title": 'fruit',
    "completed": True
}


response = requests.post('https://jsonplaceholder.typicode.com/todos', json=todos_data)

# check if it is created succesfully
if response.status_code == 201:
    print('Created!')
elif response.status_code == 404:
    print('Not Found.')