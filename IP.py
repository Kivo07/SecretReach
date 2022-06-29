import socket

user = socket.gethostname()
IP = socket.gethostbyname(user)
print("The IP address is:" + IP)
