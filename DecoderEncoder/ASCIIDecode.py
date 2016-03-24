#!/usr/bin/env python

import binascii

userinput = raw_input()

def decode(encoding):
	tempstring = ''
	tempstring2 = ''
	for i in range(0, len(userinput), encoding):
		for j in range(i,i+encoding):
			tempstring = tempstring + userinput[j]
		tempstring2 = tempstring2 + str(unichr(int(tempstring,2)))
		tempstring = ''
	print tempstring2

if ((len(userinput) % 7 == 0) and (len(userinput) % 8 == 0)):
	decode(7)
	decode(8)

elif len(userinput) % 7 == 0:
	decode(7)
elif len(userinput) % 8 ==0:
	decode(8)
else:
	print "Non-Decodable"

