import socket
import threading
def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
        except ConnectionResetError:
            break
def send_message(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))
host = '127.0.0.1'
port = 9999
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
name = input("Enter your name: ")
client_socket.send(name.encode('utf-8'))
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
send_thread = threading.Thread(target=send_message, args=(client_socket,))
receive_thread.start()
send_thread.start()
receive_thread.join()
send_thread.join()
