#!/usr/bin/python3

import socket
from datetime import datetime


addr        = ('localhost', 6789)
max_size    = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(addr)

while True:
    data, client_addr = server.recvfrom(max_size)
    if data == b'time':
        now = str(datetime.utcnow())
        server.sendto(now.encode('utf-8'), client_addr)

server.close()
