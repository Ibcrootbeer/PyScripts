#!/usr/bin/env python

import fileinput
import sys
import os

path = "/home/aaron/Desktop/ports.conf"
path2 = "/home/aaron/Desktop/apache2.conf"
            
def ChangeSetting(setting, value):
    RemoveExtras(setting)
    exists = False
    for line in fileinput.input(path, inplace=True):
        if line.startswith(setting):
            print setting + '=' + value
            exists = True
        else:
            print line.rstrip('\n')
            
    if exists == False:
        with open(path, 'a') as sshconfig:
            sshconfig.write('\n' + setting + '=' + value)

def RemoveSetting(setting):
    for line in fileinput.input(path, inplace=True):
        if line.startswith(setting):
            print ''
        else:
            print line.rstrip('\n')

def HasPortsCall():
    check = False
    for line in fileinput.input(path2, inplace=True):
        if line.rstrip('\n') == "Include ports.conf":
            check = True
        print line.rstrip('\n')
    return check

def RemoveExtras(setting):
    found = False;
    for line in fileinput.input(path, inplace=True):
        if found:
            if line.startswith(setting):
                print ''
            else:
                print line.rstrip('\n')
        else:
            if line.startswith(setting):
                found = True;
                print line.rstrip('\n')
            else:
                print line.rstrip('\n')



#os.system("sudo service apache2 restart")