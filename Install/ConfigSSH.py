#!/usr/bin/env python

import fileinput
import sys
import os

path = "/etc/ssh/sshd_config"
            
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

def RemoveSetting(setting):
    for line in fileinput.input(path, inplace=True):
        if line.startswith(setting):
            print ''
        else:
            print line.rstrip('\n')
            
if len(sys.argv) > 5 or len(sys.argv) < 3:
    print "Incorrect number of arguments " + str(len(sys.argv))
elif len(sys.argv) == 3 and sys.argv[1] == '-p':
    ChangeSetting("Port", sys.argv[2])
elif len(sys.argv) == 3 and sys.argv[1] == '-a':
    ChangeSetting("ListenAddress", sys.argv[2])
elif len(sys.argv) == 5:
    if sys.argv[1] == '-p':
        ChangeSetting("Port", sys.argv[2])
    elif sys.argv[1] == '-a':
        ChangeSetting("ListenAddress", sys.argv[2])
    
    if sys.argv[3] == '-p':
        ChangeSetting("Port", sys.argv[4])
    elif sys.argv[3] == '-a':
        ChangeSetting("ListenAddress", sys.argv[4])
else:
    print "Are the arguments in the right order?"

os.system("sudo service ssh restart")