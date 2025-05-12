import socket

#create server socket object
serveer_socket = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
#Bind to local host and port 12345
serveer_socket.bind(('localhost', 12345))
serveer_socket.listen(1)

print("Server is listening to connections...")

conn, addr = serveer_socket.accept()
print(f"connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Client says:{data}")
    response = input("You (server):")
    conn.sendall(response.encode())

conn.close()

"""Understand Networking Fundamentals
1. Research: IP addresses, MAC addresses, TCP/UDP, DNS, ports
Here’s a quick summary to get you started:

IP Address: Identifies a device on a network (e.g., 192.168.1.5).

MAC Address: Unique hardware ID for a device's network interface (e.g., 00:1A:2B:3C:4D:5E).

TCP vs. UDP:
TCP (Transmission Control Protocol): Reliable, connection-based.

UDP (User Datagram Protocol): Faster, no connection/guarantees.

DNS: Translates domain names (like google.com) into IP addresses.

Ports: Logical endpoints (e.g., port 80 for HTTP, port 443 for HTTPS).

2. Study how data moves through a network

Learn the OSI Model: 7 layers (Physical → Application).

Watch how a packet moves from one device to another.

Tools: Wireshark (for real packet observation)."""