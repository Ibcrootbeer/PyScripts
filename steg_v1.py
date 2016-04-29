#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

counter = 0
interval = 0
bit = True
retrieval = False
out_f = ""
in_f = ""
store = False
offset = 0
bits_backwards = False

while counter < len(sys.argv):
	i = sys.argv[counter]
	if(i[:2] == "-o"):  # set offset to ? 
		 offset = int(i[2:])
	if(i[:2] =="-b"): # use the bit method
		bit = True
	if(i[:2] == "-r"): # retrieve hidden data
		retrieval = True
	if(i[:2] == "-B"): # use the byte method
		bit = False
	if(i[:2] == "-s"): # store and hide
		store = True
	if(i[:2] == "-i"): # set interval to file
		interval = int(i[2:])
	if(i[:2] == "-w"): # set wrapper to file
		in_f = i[2:]
	if(i[:2] == "-h"): # set hidden file to
		out_f = i[2:]
	if(i == "--revers-bits"):
		bits_backwards = True
	if(i == "--read-backwards"):
		pass
	counter += 1

print offset
counter = 0
if(out_f != ''):
	out_f = open(out_f, 'w')
	
bit_counter = 0
bit = 0
bits = [1, 2, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7]
if bits_backwards:
	bits.reverse()
	
bits.reverse()

if(in_f != ''):
	read_data = ''
	in_f = open(in_f, 'r')
	# jump to offset
	n = in_f.read(offset)
	n = in_f.read(1)
	while(n != ''):
		if(bit):
			if(bit_counter == 7):
				read_data += chr(bit)
				bit_counter = 0
			else:
				bit_counter += 1
			bit += bits[bit_counter] if ord(n) & 0x01 else 0
		else:
			read_data += n
			
		in_f.read(interval - 1)
		n = in_f.read(1)

	print read_data
