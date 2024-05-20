import socket

HOST = '192.168.0.216'
PORT = 7483

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello World!".encode('utf-8'))
print(socket.recv(1024))