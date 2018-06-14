#!/usr/bin/python3

import socket
from datetime import datetime
from time import sleep

addr        = ('localhost', 6789)
max_size    = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    sleep(5)
    client.sendto(b'time', addr) # a bytes-like object is required, not 'str'
    data, server_addr = client.recvfrom(max_size)
    print('Client read', data)

client.close()
