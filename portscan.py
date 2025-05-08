 import socket

target = input("IPv4: ")
port = int(input("PORT: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)
code = sock.connect_ex((target, port))
if code == 0:
	print (f"Port {port} Open.")
else:
	print (f"Port {port} Close.")
