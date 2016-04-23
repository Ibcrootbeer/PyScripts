#!/usr/bin/env python

import sys

'''
Fancy Rot13.
No command line arguments will decode the message 26 times.
Adding a number will rotate the message that many times.
Caesar.py
Caesar.py 10
'''


#Same as Rot13 except for one difference that it can do a variable number of rotations.
def rotate(message, rotations):
    output = []
    for i in message.lower():
        if ord(i) >= 97 and ord(i) <= 97 + 25:
            output.append(unichr((ord(i) - 97 + rotations) % 26 + 97))
        else:
            output.append(i)
    for i in range(len(output)):
        if message[i].isupper():
            output[i] = output[i].upper()
    return ''.join(output)

#This is a horrible thing and I hate it
if __name__ == "__main__":
    #Command line stuff.
    if len(sys.argv) > 1 and sys.argv[1] == '-test':
        userinput = raw_input("In: \t\t")
        print "Rotated: \t" + rotate(userinput, 1)
    elif len(sys.argv) == 1:
        userinput = raw_input()
        for i in range(1,26):
            print rotate(userinput, i)
    elif len(sys.argv) == 2 :
        check = True
        try:
            int(sys.argv[1])
        except:
            print "That is not a number"
            check = False
        if check:
            print rotate(raw_input(), int(sys.argv[1]))
    else:
        print "Too many arguments"