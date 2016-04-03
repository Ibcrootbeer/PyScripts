#!/usr/bin/env python

import sys

'''
Dvorak.py -e
Dvorak.py -d
'''

#Encodes the message that is put in.
def encode(message, combined):
	output = ''
	#Adds the dvorak key for every caracter in message.
	for char in message:
		output += combined[char]
	return output

#Decodes the message that is put in.
def decode(message, combined):
	output = ''
	#Goes through all the characters in message and adds the corresponding key to output.
	for char in message:
			for key, value in combined.iteritems():
					if value == char:
							output += key
	return output
#Builds the dictionary between the two input strings for the layouts.
def combine(layout1, layout2):
	output = {}
	for i in range(len(layout1)):
		output[layout1[i]] = layout2[i]
	return output

#All keys from both layouts. If you wanted to add more layouts it would be trivial.
standard = 	" `1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?"
dvorak = 	" `1234567890[]',.pyfgcrl/=\\aoeuidhtns-;qjkxbmwvz~!@#$%^&*(){}\"<>PYFGCRL?+|AOEUIDHTNS_:QJKXBMWVZ"


combined = combine(standard, dvorak)

#Command line stuff.
if len(sys.argv) != 2:
	print "Incorrect number of arguments."
elif sys.argv[1] == '-e':
	print encode(raw_input(), combined)
elif sys.argv[1] == '-d':
	print decode(raw_input(), combined)
elif sys.argv[1] == '-test':
	userinput = raw_input("In: \t\t")
	encoded = encode(userinput, combined)
	decoded = decode(encoded, combined)
	print "Encoded: \t" + encoded
	print "Decoded: \t" + decoded

	