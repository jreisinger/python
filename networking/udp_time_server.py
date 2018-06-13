#!/usr/bin/python3

from datetime import datetime
import socket

address = ('localhost', 6789)
max_size = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(address)

while True:
    data, client_addr = server.recvfrom(max_size)
    if data == b'time':
        now = str(datetime.utcnow())
        now = now.encode('utf-8')
        server.sendto(now, client_addr)

server.close()
