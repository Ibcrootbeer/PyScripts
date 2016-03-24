#!/usr/bin/env python

import binascii

userinput = raw_input()

def decode(encoding):
	output = ''
	for i in range(0, len(userinput), encoding):
		output = output + str(unichr(int(userinput[i:i+encoding],2)))
	print output

if ((len(userinput) % 7 == 0) and (len(userinput) % 8 == 0)):
	decode(7)
	decode(8)

elif len(userinput) % 7 == 0:
	decode(7)
elif len(userinput) % 8 == 0:
	decode(8)
else:
	print "Non-Decodable"

