#!/usr/bin/env python

import fileinput
import os

pathssh = ""
path = ""


def ChangeSetting(setting, value):
    exists = False
    for line in fileinput.input(path, inplace=True):
        if line.startswith(setting):
            print setting + ' ' + value
            exists = True
        else:
            print line.rstrip('\n')
            
    if exists == False:
        with open(path, 'a') as sshconfig:
            sshconfig.write('\n' + setting + ' ' + value)

os.system("sudo echo \"Shadow!\" > /var/www/html/index.html")
os.system("sudo touch /etc/motd")
os.system("sudo echo \"Shadow!\" > /etc/motd")
for line in fileinput.input("/etc/vsftpd.conf", inplace=True):
    if line.startswith("#ftpd_banner=") or line.startswith("ftpd_banner="):
        print "ftpd_banner=Shadow!"
    else:
        print line.rstrip('\n')
os.system("sudo mysql -u root -h localhost -p")