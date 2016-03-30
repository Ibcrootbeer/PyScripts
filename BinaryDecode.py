#!/usr/bin/env python

import sys

userinput = raw_input()

def decode(encodinglength):
	output = ''
	for i in range(0, len(userinput), encodinglength):
		output += str(unichr(int(userinput[i:i+encodinglength],2)))
	print output

def default():
	if ((len(userinput) % 7 == 0) and (len(userinput) % 8 == 0)):
		decode(7)
		decode(8)

	elif len(userinput) % 7 == 0:
		decode(7)
	elif len(userinput) % 8 == 0:
		decode(8)

try:
	if sys.argv[1] == "-a":
		for i in range(1,100):
			try:
				decode(i)
			except:
				pass
	elif sys.argv[1] == "-n":
		try:
			decode(int(sys.argv[2]))
		except:
			pass
	else:
		default()
except:
	default()
