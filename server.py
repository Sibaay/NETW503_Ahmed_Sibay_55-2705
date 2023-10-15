import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 5605
server_socket.bind((host, port))
server_socket.listen(1)  # Only one client at a time

print("Server is listening for a connection...")

client_socket, client_address = server_socket.accept()

while True:
    message = client_socket.recv(1024).decode()
    if not message:
        break
    print(f"Received: {message}")
    response = message.upper()
    client_socket.send(response.encode())

client_socket.close()
server_socket.close()