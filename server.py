import socket
import threading
clients = {}
def handle_client(client_socket, client_name):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            broadcast_message(f'{client_name}: {data}')
        except ConnectionResetError:
            break
    del clients[client_name]
    client_socket.close()
    broadcast_message(f'{client_name} has left the chat.')
def broadcast_message(message):
    for client_socket in clients.values():
        try:
            client_socket.send(message.encode('utf-8'))
        except ConnectionResetError:
            pass
host = '127.0.0.1'
port = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print(f'Server listening on {host}:{port}...')

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Connection established with {client_address}')
    client_name = client_socket.recv(1024).decode('utf-8')
    clients[client_name] = client_socket
    threading.Thread(target=handle_client, args=(client_socket, client_name)).start()
