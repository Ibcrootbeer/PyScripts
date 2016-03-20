#!/usr/bin/env python
#TODO Make system give me the username
#TODO Make system give me all users on machine and then preform this on all of them

#To get the alias list run this:
#{ ls /bin; ls /usr/bin; } | sort > /home/aaron/Desktop/PyScripts/BASH/aliases.txt
#TODO Run this then start script


import fileinput
#TODO Eventually only create one file that will execute so aliases.txt is not needed

for line in fileinput.input("/home/aaron/Desktop/PyScripts/BASH/aliases.txt", inplace=True):
	output = "\tbashrc.write('alias " + line.rstrip('\n') + "=\\'exit\\'\\n')"
	print output

#TODO Mabey make it force close any open terminals.
#TODO End goal is that this generates the entire "Are you BASHful.py" file and ten runs it.
