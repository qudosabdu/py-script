

import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = '127.0.0.1' # localhost
port = 12345

#connect to the server
client_socket.connect((host, port))

# send a message to the server
message = "Hello, how are you?"
client_socket.send(message.encode('utf-8'))

# receive data from the server
data = client_socket.recv(1024)

print(f"Received from server: {data.decode('utf-8')}")
# close the connection
client_socket.close()
# The client script creates a socket object and connects to the server. It then sends a message to the server and receives a response. Finally, the connection is closed.

