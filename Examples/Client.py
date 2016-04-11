#!/usr/bin/env python

import socket


#Created the socket.
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5444)

#Connects to socket to the server.
clientsocket.connect(server_address)

#This message is sent to the server.
clientsocket.send(raw_input("Please enter message to send to server."))

#This prints any responce from the server
print clientsocket.recv(5444)

#Cleans up the socket
clientsocket.close()