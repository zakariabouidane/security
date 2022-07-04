import socket 

# variablename = commands or value
# input('your message') to enter data
# int() to covert some type to integer 
port = int(input('Enter port number : '))
test = socket.getservbyport(port)
print(test)