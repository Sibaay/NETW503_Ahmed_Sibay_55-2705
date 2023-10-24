import socket
import threading

PORT = 5605
ADDR = ('127.0.0.1', PORT)
clients = []  

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append((conn, addr))  

    while True:
        message = conn.recv(1024).decode()
        if not message:
            break
        print(f"Received from {addr}: {message}")
        response = message.upper()
        conn.send(response.encode())

        if "CLOSE SOCKET" in message:
            conn.close()
            clients.remove((conn, addr))
            print(f"[CONNECTION CLOSED] {addr}")
            break

def main():
    print("Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()

    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

        print(f"[ACTIVE CONNECTIONS] {len(clients)}")

if __name__ == "__main__":
    main()
