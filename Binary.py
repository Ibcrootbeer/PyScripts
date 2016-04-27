#!/usr/bin/env python

import sys

'''
no args   --- Decodes input with 7 and/or 8 encoding length
-a        --- Decodes input with 1-100 encoding length
-d <val>  --- Decodes with specified encoding length
-e <val>  --- Encodes with specified encoding length
'''

#This decodes the binary message. Encodinglength is how I make it do a variable ammout of zeros.
def decode(encodinglength, message):
    output = ''
    for i in range(0, len(message), encodinglength):
        #Chunks up the binary and turns it into characters.
        output += str(unichr(int(message[i:i + encodinglength], 2)))
    return output

def shortDecode(message):
    userinput = message
    if ((len(userinput) % 7 == 0) and (len(userinput) % 8 == 0)):
        print decode(7, userinput)
        print decode(8, userinput)
    elif len(userinput) % 7 == 0:
        print decode(7, userinput)
    elif len(userinput) % 8 == 0:
        print decode(8, userinput)
        
def longDecode(message):
    for i in range(1, 100):
        try:
            print decode(i, message)
        except:
            pass

#This is used for encoding so that the outputed binary has the correct number of zeros.
def fillZeros(length, binary):
    while len(binary) < length:
        binary = "0" + binary
    return binary

#Encodes the message that is put in into binary. Again encodinglength is used to set a variable ammout of zeros.
def encode(encodinglength, message):
    binarylist = []
    output = ''
    for char in message:
        binarylist.append(format(ord(char), 'b'))
    for binary in binarylist:
        if len(binary) < encodinglength:
            binary = fillZeros(encodinglength, binary)
            output += binary
        else:
            output+= binary
    return output

#This is a horrible thing and I hate it. If this is the main program it will run whatever is after this.
if __name__ == "__main__":
    coutnter = 0;
    message = raw_input()
    for i in range(len(sys.argv)):
        if len(sys.argv) == 1:
            shortDecode(message)
            break
        if sys.argv[i] == '-a':
            longDecode(message)
            break
        try:
            if sys.argv[i] == '-d':
                decode(sys.argv[2], message)
                break
            if sys.argv[i] == '-e':
                encode(sys.argv[2], message)
                break
        except:
            print "Not enough arguments"