#!/usr/bin/env python

import os

os.system("sudo apt-get update")
print "Finished updating existing packages"

os.system("sudo apt-get -y install apache2")
os.system("sudo echo \"Shadow!\" > /var/www/html/index.html")
print "Finished installing apache2"

os.system("sudo apt-get -y install openssh-server")
os.system("sudo touch /etc/motd")
os.system("sudo echo \"Shadow!\" > /etc/motd")
print "Finished installing openssh-server"

os.system("sudo apt-get -y install vsftpd")
print "Finished installing vsftpd"

os.system("sudo apt-get -y install mysql-server")

import fileinput
for line in fileinput.input("/etc/mysql/my.cnf", inplace=True):
	if line.rstrip('\n') == "bind-address\t\t= 127.0.0.1":
		print "bind-address\t\t= 0.0.0.0"
	else:
		print line.rstrip('\n')
os.system("sudo service mysql restart")
print "Finished installing mysql-server"

os.system("netstat -lntu")
