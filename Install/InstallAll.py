#!/usr/bin/env python

import os
import fileinput

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
for line in fileinput.input("/etc/vsftpd.conf", inplace=True):
	if line.startswith("#ftpd_banner=") or line.startswith("ftpd_banner="):
		print "ftpd_banner=Shadow!"
	else:
		print line.rstrip('\n')
os.system("sudo service vsftpd restart")
print "Finished installing vsftpd"

os.system("sudo apt-get -y install mysql-server")

for line in fileinput.input("/etc/mysql/my.cnf", inplace=True):
	if line.rstrip('\n') == "bind-address\t\t= 127.0.0.1":
		print "bind-address\t\t= 0.0.0.0"
	else:
		print line.rstrip('\n')
os.system("sudo service mysql restart")
os.system("sudo mysql -u root -h localhost -p")
print "Finished installing mysql-server"

os.system("netstat -lntu | grep :21")
os.system("netstat -lntu | grep :22")
os.system("netstat -lntu | grep :80")
os.system("netstat -lntu | grep :3306")
