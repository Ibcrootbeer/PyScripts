#!/usr/bin/env python

#To get the alias list run this:
#{ ls /bin; ls /usr/bin; } | sort > /home/aaron/Desktop/PyScripts/aliases.txt

import fileinput

s = 'hello world'
print s

for line in fileinput.input("/home/aaron/Desktop/PyScripts/aliases.txt", inplace=True):
	output = "\tbashrc.write('alias " + line.rstrip('\n') + "=\\'exit\\'\\n')"
	print output



'''
with open("/home/aaron/Desktop/PyScripts/aliases.txt", 'r') as inputFile, open("/home/aaron/Desktop/PyScripts/aliasestest.txt", 'w') as outputFile:
	for line in inputFile:
		output = "\tbashrc.write('alias " + line.rstrip('\n') + "=\\'exit\\'\\n')\n"
		outputFile.write(output)
'''
