import socket

#create client socket
client_socket = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True:
    message = input("You(client):")
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024).decode()
    print(f"Server says: {data}")

client_socket.close()