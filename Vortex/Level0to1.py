#!/usr/bin/env python

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5444)
sock.connect(server_address)
sock.send("this")
print sock.recv(5444)
sock.close()