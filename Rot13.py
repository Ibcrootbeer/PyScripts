#!/usr/bin/env python

import sys
'''
There are no command line arguments because to decodeing something encoded is just to encode it again.
Rot13.py
'''

#Does the rotate on the input message.
def rotate(message):
    output = []
    #Goes through each letter and if its not a-z it will ignore it. Also ignores caps.
    for i in message.lower():
        if ord(i) >= 97 and ord(i) <= 97 + 25:
            #If it is a-z it will preform a rotate 13 on it i.e. a -> n
            output.append(unichr((ord(i) - 97 + 13) % 26 + 97))
        else:
            output.append(i)
    #Re-capitolizes things.
    for i in range(len(output)):
        if message[i].isupper():
            output[i] = output[i].upper()
    return ''.join(output)

#Command line stuff.
if len(sys.argv) > 1 and sys.argv[1] == '-test':
    userinput = raw_input("In: \t\t")
    encoded = rotate(userinput)
    decoded = rotate(encoded)
    print "Encoded: \t" + encoded
    print "Decoded: \t" + decoded
elif len(sys.argv) == 1:
    print rotate(raw_input())
else:
    print "Too many arguments"