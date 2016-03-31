#!/usr/bin/env python

import os
os.system("sudo apt-get -y purge apache2")
os.system("sudo apt-get -y purge openssh-server")
os.system("sudo rm /etc/motd")
os.system("sudo rm ~/.ssh/known_hosts")
os.system("sudo apt-get -y purge vsftpd")
os.system("sudo apt-get -y purge mysql*")
os.system("sudo rm /usr/bin/mysql -R")
os.system("sudo rm /var/lib/mysql -R")
os.system("sudo rm /etc/mysql -R")
os.system("sudo rm /etc/my.cnf.rmp")

