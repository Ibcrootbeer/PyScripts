#!/usr/bin/env python

import socket

#Creates the socket.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Makes the socket reusable for easy testing.
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 5444)
#binds the socket at the specified server on port 5444
serversocket.bind(server_address)

#Sets the number of clients that will be listened for?
serversocket.listen(5)

while True:
    #Don't know why this is continualy created.
    connection, address = serversocket.accept()
    #this is the message rceived from the client.
    buf = connection.recv(5444)
    if len(buf) > 0:
        if buf == "stop":
            break
        print "Recieved this from the client:\n" + buf
        #This is how to respond to the client.
        connection.sendall("Reply from server.")

serversocket.close()