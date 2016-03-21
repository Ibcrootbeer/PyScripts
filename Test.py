#!/usr/bin/env python

#Currently run this to make this work.
#Test.py >> /home/aaron/.bashrc

import subprocess


aliasesProcess = subprocess.Popen("{ ls /bin; ls /usr/bin; } | sort", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in aliasesProcess.stdout.readlines():
	if line.rstrip('\n') == "vi":
		print ""
	elif line.rstrip('\n') == "vim":
		print ""
	else:
		print "alias " + line.rstrip('\n') + "=\'exit\'"

nameProcess = subprocess.Popen("echo $USER", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
name = nameProcess.stdout.readline()

print "alias plzfix='vim /home/" + name.rstrip('\n') + "/.bashrc'"
print "alias plzfixthis='vi /home/" + name.rstrip('\n') + "/.bashrc'"
print "alias sudo='exit'"
print "alias cd='exit'"
print "alias ls='exit'"
print "alias alias='exit'"


