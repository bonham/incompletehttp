import socket
import struct
import time

# tcp_server.py
def handler(client_sock, addr):
    try:
        print('new client from %s:%s' % addr)
        time.sleep(1)
    finally:
        client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
            struct.pack('ii', 1, 0))
        client_sock.close()   # close current connection directly

if __name__ == '__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', 8844))
    sock.listen(5)

    while 1:
        client_sock, addr = sock.accept()
        handler(client_sock, addr)