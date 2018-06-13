#!/usr/bin/env python3

""" 
With plain sockets, you need to start the server first. With ZeroMQ, you can
start either the server or client first.
"""

import zmq
from datetime import datetime
from time import sleep

host = "127.0.0.1"
port = 6789

context = zmq.Context()
client  = context.socket(zmq.REQ)

client.connect("tcp://%s:%s" % (host, port))
print("Client started at", datetime.utcnow())

while True:
    sleep(5)
    request = b"time"
    client.send(request)
    reply = client.recv()
    print("Client received %s" % reply)
