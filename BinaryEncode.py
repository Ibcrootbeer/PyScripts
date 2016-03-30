#!/usr/bin/env python

import sys

binarylist = []

userinput = raw_input()

for char in userinput:
	binarylist.append(format(ord(char), 'b'))

def fill(length, binary):
	while len(binary) < length:
		binary = "0" + binary
	return binary

def encode(length):
	output = ''
	for binary in binarylist:
		if len(binary) < length:
			binary = fill(length, binary)
			output += binary
		else:
			output+= binary
	return output

if len(sys.argv) == 1:
	print encode(7)

else:
	try:
		if(sys.argv[1] == "-n"):
			print encode(int(sys.argv[2]))
	except:
		pass

