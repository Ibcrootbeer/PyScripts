#!/usr/bin/env python

import fileinput
import sys
import os

path = "/etc/mysql/my.cnf"
            
def ChangeSetting(setting, value):
    exists = False
    for line in fileinput.input(path, inplace=True):
        if line.startswith(setting):
            print setting + '\t\t= ' + value
            exists = True
        else:
            print line.rstrip('\n')
            
    if exists == False:
        with open(path, 'a') as sshconfig:
            sshconfig.write('\n' + setting + '\t\t= ' + value)

def RemoveSetting(setting):
    for line in fileinput.input(path, inplace=True):
        if line.startswith(setting):
            print ''
        else:
            print line.rstrip('\n')
            
if len(sys.argv) > 5 or len(sys.argv) < 3:
    print "Incorrect number of arguments " + str(len(sys.argv))
elif len(sys.argv) == 3 and sys.argv[1] == '-p':
    ChangeSetting("port", sys.argv[2])
elif len(sys.argv) == 3 and sys.argv[1] == '-a':
    ChangeSetting("bind-address", sys.argv[2])
elif len(sys.argv) == 5:
    if sys.argv[1] == '-p':
        ChangeSetting("port", sys.argv[2])
    elif sys.argv[1] == '-a':
        ChangeSetting("bind-address", sys.argv[2])
    
    if sys.argv[3] == '-p':
        ChangeSetting("port", sys.argv[4])
    elif sys.argv[3] == '-a':
        ChangeSetting("bind-address", sys.argv[4])
else:
    print "Are the arguments in the right order?"

os.system("sudo service mysql restart")