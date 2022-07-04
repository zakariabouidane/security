import socket

portname = input('Enter port name : ')
test = socket.getservbyname(portname)
print(test)