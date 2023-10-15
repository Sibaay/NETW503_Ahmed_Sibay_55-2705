import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 5605
client_socket.connect((host, port))

while True:
    message = input("Enter your message (or type 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print(f"Server Response: {response}")

client_socket.close()