#!/usr/bin/env python

import sys

def readFileAsBinary(path):
    output = ''
    with open(path, "rb") as filein:
        byte = filein.read(1)
        while byte != '':
            output += '{0:08b}'.format(ord(byte))
            byte = filein.read(1)
    return output

def xor(binaryMessage, binaryKey):
    output = ''
    for i in range(len(binaryMessage)):
        output += str(int(binaryMessage[i]) ^ int(binaryKey[i]))
    return output

def decodeBinary(message):
    output = ''
    for i in range(0, len(message), 8):
        output += str(chr(int(message[i:i + 8], 2)))
    return output

def encodeBinary(message):
    output = ''
    for byte in range(len(message)):
        output += '{0:08b}'.format(ord(message[byte]))
    return output

def debugPrint():
    message = readFileAsBinary("ciphertext")
    key = readFileAsBinary("key")
    xord = xor(message, key)
    xord2 = xor(xord, key)
    xord3 = xor(xord2, key)
    print "Message:\t" + message
    print "Key:\t\t" + key
    print "XOR:\t\t" + decodeBinary(xord)
    print "XORXOR:\t\t" + xord2
    print "XORXORXOR:\t" + decodeBinary(xord3)
    print "Done"

try:
    if sys.argv[1] == "-test":
        debugPrint()
except:
    message = encodeBinary(raw_input())
    key = readFileAsBinary("key")
    xord = xor(message, key)
    sys.stdout.write(decodeBinary(xord))