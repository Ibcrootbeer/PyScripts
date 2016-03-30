#!/usr/bin/env python

# a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
# 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

import sys

def printf(strin):
	sys.stdout.write(strin)

def combine(ch1, ch2):
	return ((ord(ch1)-97) + (ord(ch2) - 97)) % 26

def encode():
	key = "KEY"
	testkey = key.replace(" ", '').lower()


	userinput = raw_input()
	testinput = userinput.lower()


	counter = 0
	output = []
	for i in testinput:
		if ord(i) < 97 or ord(i) > 97 + 26:
			output.append(i)
		else:
			output.append(str(unichr(combine(i, testkey[counter]) + 97)))
			counter = (counter + 1) % len(testkey)
	for i in range(0, len(output)):
		if userinput[i].isupper():
			output[i] = output[i].upper()

	print ''.join(output)

encode()
