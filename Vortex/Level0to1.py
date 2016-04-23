#!/usr/bin/env python

import socket
import struct

def unpack(userinput):
    #This unpacks it with a buffer on the receiv of 4 bytes and then returns the 1st entry of the struct
    return struct.unpack("<I", userinput)[0]
def pack(userinput): 
    #& is a bitwise operation doing something nifty. Find another way to look at it.
    return struct.pack("<I", userinput & 0xffffffff)

sock = socket.socket()
sock.connect(("vortex.labs.overthewire.org", 5842))
sums = 0

for i in range(4):
    intin = unpack(sock.recv(4))
    print "Int " + str(i + 1) + ": " + str(intin)
    sums += intin
    
print "Sum of ints: " + str(sums)
sock.send(str(pack(sums)))

print sock.recv(5000)

sock.close()
