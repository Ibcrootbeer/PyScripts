#!/usr/bin/env python

import sys

def decode(encodinglength, message):
    output = ''
    for i in range(0, len(message), encodinglength):
        output += str(unichr(int(message[i:i + encodinglength], 2)))
    return output

def default():
    userinput = raw_input()
    if ((len(userinput) % 7 == 0) and (len(userinput) % 8 == 0)):
        decode(7)
        decode(8)

    elif len(userinput) % 7 == 0:
        decode(7)
    elif len(userinput) % 8 == 0:
        decode(8)

def fillzeros(length, binary):
    while len(binary) < length:
        binary = "0" + binary
    return binary

def encode(encodinglength, message):
    binarylist = []
    output = ''
    for char in message:
        binarylist.append(format(ord(char), 'b'))
    for binary in binarylist:
        if len(binary) < encodinglength:
            binary = fillzeros(encodinglength, binary)
            output += binary
        else:
            output+= binary
    return output

if len(sys.argv) == 2 and sys.argv[1] == '-test':
    encoded = encode(7, raw_input("In:\t\t"))
    decoded = decode(7, encoded)
    print "Encoded:\t" + encoded
    print "Decoded:\t" + decoded