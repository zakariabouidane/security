import socket

domain = input('Enter the domain name : ')
ip = socket.gethostbyname(domain)
print("IP is :"); print(ip)