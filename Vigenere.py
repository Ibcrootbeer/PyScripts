#!/usr/bin/env python

import sys

def printf(strin):
	sys.stdout.write(strin)

def encrypt(char1, char2):
	return ((ord(char1) - 97) + (ord(char2) - 97)) % 26

def decrypt(char1, char2):
	return ((ord(char1) - 97) - (ord(char2) - 97)) % 26

def crypt(message, key, conversion):
	testkey = key.replace(" ", '').lower()
	counter = 0
	output = []
	for i in message.lower():
		if ord(i) < 97 or ord(i) > 97 + 26:
			output.append(i)
		else:
			if conversion == "encrypt":
				output.append(str(unichr(encrypt(i, testkey[counter]) + 97)))
			else:
				output.append(str(unichr(decrypt(i, testkey[counter]) + 97)))
			counter = (counter + 1) % len(testkey)
	for i in range(0, len(output)):
		if message[i].isupper():
			output[i] = output[i].upper()
	print ''.join(output)

if len(sys.argv) != 3:
	print "Incorrect number of arguments."
elif sys.argv[1] == '-e':
	crypt(raw_input(), sys.argv[2], "encrypt")
elif sys.argv[1] == '-d':
	crypt(raw_input(), sys.argv[2], "decrypt")
else:
	print "Are the arguments in the wrong order?"
