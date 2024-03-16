# Request library is used to send HTTP requests to the server

import requests
#  Make a GET request to the server
response = requests.get('http://jsonplaceholder.typicode.com/posts')

# check if the request was succesfull ( status code 200)
if response.status_code == 200:
    print(response.json())
else:
    print("Error in request")

# The requests library is used to send HTTP requests to the server. In this example, a GET request is made to the server and the response is printed. The status code of the response is checked to see if the request was successful. If the status code is 200, the response is printed. Otherwise, an error message is printed.
