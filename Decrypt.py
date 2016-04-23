#!/usr/bin/env python

import Caesar
import Binary

userinput = raw_input()

print "user input: " + userinput

encr = Caesar.rotate(userinput, 13)
decr = Caesar.rotate(encr, 13)

print Binary.shortdecode(userinput)

print encr
print decr