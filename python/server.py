import socket

s = socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.1.29", 5000))
s.listen(5)

while 1:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    