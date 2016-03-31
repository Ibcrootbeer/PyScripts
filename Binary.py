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

if len(sys.argv) > 3:
    print "Too many arguments."
elif len(sys.argv) == 2 and sys.argv[1] == '-test':
    encoded = encode(7, raw_input("In:\t\t"))
    decoded = decode(7, encoded)
    print "Encoded:\t" + encoded
    print "Decoded:\t" + decoded
elif len(sys.argv) == 2 and sys.argv[1] == '-e':
        print encode(7, raw_input())
elif len(sys.argv) == 2 and sys.argv[1] == '-d':
    userinput = raw_input()
    if ((len(userinput) % 7 == 0) and (len(userinput) % 8 == 0)):
        print decode(7, userinput)
        print decode(8, userinput)

    elif len(userinput) % 7 == 0:
        print decode(7, userinput)
    elif len(userinput) % 8 == 0:
        print decode(8, userinput)
elif len(sys.argv) == 3:
    check = True
    try:
        int(sys.argv[2])
    except:
        print "Argument is not a number."
        check = False
    if sys.argv[1] == '-e' and check == True:
        print encode(int(sys.argv[2]), raw_input())
    elif sys.argv[1] == '-d' and check == True:
        print decode(int(sys.argv[2]), raw_input())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        