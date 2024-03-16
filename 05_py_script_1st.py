# day five
#  socket library

import socket
# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = '127.0.0.1' # localhost
port = 12345

# bind the server to the host and port
server_socket.bind((host, port))

# listen for incoming connections
server_socket.listen(5)
print(f"Connection listening on {host}:{port}")

# accept the connection
client_socket, addr = server_socket.accept()

print("Got a connection from %s" % str(addr))

# send a thank you message to the client
msg = "Thank you for connecting" + "\r\n"
client_socket.send(msg.encode('ascii'))

# close the connection
client_socket.close()

# close the server
server_socket.close()
# The socket library is a low-level networking interface. It is used to create a socket object that can listen for incoming connections. The socket object is then bound to a host and port, and the server is set to listen for incoming connections. When a connection is made, the server accepts the connection and sends a message to the client. Finally, the connection is closed and the server is closed.



