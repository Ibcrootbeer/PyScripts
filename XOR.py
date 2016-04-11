#!/usr/bin/env python

encodingTable = "abcdefghijklmnopqrstuvwxyz012345"

message = "thisismymessage"

key = "password"


def fillzeros(binary):
    while len(binary) < 5:
        binary = "0" + binary
    return binary

def toBinary(message):
    output = ''
    for char in message:
        if char in encodingTable:
            output += fillzeros(format(encodingTable.index(char), 'b'))
    return output

def toXOR(message):
    output = ''
    counter = 0
    for i in range(len(toBinary(message))):
        if toBinary(message)[i] != toBinary(key)[counter % len(toBinary(key))]:
            output += '1'
            counter += 1
        else:
            output += '0'
            counter += 1
    return output

print "Message: \t" + message
print "Key: \t\t" + key
print "Message Binary: " + toBinary(message)
#print "Key Binary: \t" + toBinary(key) + toBinary(key) + toBinary(key) + toBinary(key) + toBinary(key)
out = ''
while len(out) < len(toBinary(message)):
    out += toBinary(key)
print "Key Binary: \t" + out
print "XOR: \t\t" + toXOR(message)
