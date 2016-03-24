#!/usr/bin/env python

import os
os.system("sudo apt-get -y remove apache2")
os.system("sudo apt-get -y remove openssh-server")
os.system("sudo rm /etc/motd")
os.system("sudo apt-get -y remove vsftpd")
os.system("sudo apt-get -y remove mysql-server")
