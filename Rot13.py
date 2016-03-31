#!/usr/bin/env python

import sys

def encode(message):
    output = []
    for i in message.lower():
        if ord(i) >= 97 and ord(i) <= 97 + 25:
            output.append(unichr((ord(i) - 97 + 13) % 26 + 97))
        else:
            output.append(i)
    for i in range(len(output)):
        if message[i].isupper():
            output[i] = output[i].upper()
    return ''.join(output)

if len(sys.argv) > 1 and sys.argv[1] == '-test':
    userinput = raw_input("In: \t\t")
    encoded = encode(userinput)
    decoded = encode(encoded)
    print "Encoded: \t" + encoded
    print "Decoded: \t" + decoded
elif len(sys.argv) == 1:
    print encode(raw_input())
else:
    print "Too many arguments"