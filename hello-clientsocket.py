import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('elfu.de', 8844))
chunk = s.recv(1024)

print(chunk)

