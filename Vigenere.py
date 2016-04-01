#!/usr/bin/env python

import sys

'''
All of my math for the ascii code is done on a scale from 0 to 25 so that's why you see the -97's.
a=0 b=1 ... So to encrypt it adds the two values together so if the key starts with b and the input starts with c it adds together 1 + 2 to get 3 so it comes out as d. 
EXAMPLES
Vigenere.py -e <KEY>
Vigenere.py -d <KEY>
'''

#Used to tuncate the code a bit. Just so I didnt have to write this out every time.
def printf(strin):
	sys.stdout.write(strin)

#Adds the two values for the characters together on a mod of 26 to wrap back around if the values exceed 26.
def encrypt(char1, char2):
	return ((ord(char1) - 97) + (ord(char2) - 97)) % 26

#Decryption is the reverse of encryption so instead of add it subtracts.
def decrypt(char1, char2):
	return ((ord(char1) - 97) - (ord(char2) - 97)) % 26

#This function should really be split into two functions but it takes in the message and key and a 3rd condition to specify encryption or decryption.
def crypt(message, key, conversion):
	#His examples did not account for spaces so I remove them.
	testkey = key.replace(" ", '').lower()
	counter = 0
	output = []
	#I do not care about capitolization at the moment so I just lowercase everything
	for i in message.lower():
		#If the characer it not a-z ignore it.
		if ord(i) < 97 or ord(i) > 97 + 26:
			output.append(i)
		else:	
			#This is where stuff actually happens. It encrypts/decrypts the current two characters and then increments the counter. The counter is used for traversing the key alongside the main message.
			if conversion == "encrypt":
				output.append(str(unichr(encrypt(i, testkey[counter]) + 97)))
			else:
				output.append(str(unichr(decrypt(i, testkey[counter]) + 97)))
			counter = (counter + 1) % len(testkey)
	#Since I didn't care about the capitolization before I need to re-capitolize things do this just goes through and changes them back if they were capitolized.
	for i in range(len(output)):
		if message[i].isupper():
			output[i] = output[i].upper()
	return ''.join(output)

#This is just all the command line stuff. Don't worry about the -test parameter I use that for testing it in my IDE.
if len(sys.argv) == 2 and sys.argv[1] == '-test':
	userinputphrase = raw_input("Phrase: ")
	userinputkey = raw_input("Key: ")
	encrypted = crypt(userinputphrase, userinputkey, "encrypt")
	decrypted = crypt(encrypted, userinputkey, "decrypt")
	print "Encrypted: " + encrypted
	print "Decrypted: " + decrypted
elif len(sys.argv) != 3:
	print "Incorrect number of arguments."
elif sys.argv[1] == '-e':
	print crypt(raw_input(), sys.argv[2], "encrypt")
elif sys.argv[1] == '-d':
	print crypt(raw_input(), sys.argv[2], "decrypt")
else:
	print "Are the arguments in the wrong order?"
