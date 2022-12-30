import socket

# The IP of the server
HOST = '192.168.1.9'
PORT = 9090
# myip.is

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send('Hello world'.encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))