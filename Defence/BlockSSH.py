#!/usr/bin/env python

import subprocess
import os
import time

'''
Monitors and closes any incoming ssh atempts. It will preserve any that are opened before this is run.
Should be easy enough to add in ftp and mysql and make this a overall defence. Tho it isn't really effective against someone that knows what they are doing.
TURN THIS INTO A SERVICE
'''


#The three main lists.
processes = []
protected = []
tokill = []

#Gets the open ssh processes. Should refactor this to incluse removeEmpty.
def gatherInfo(listin):
    getprocesses = subprocess.Popen("ps aux | grep sshd:", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in getprocesses.stdout.readlines():
        if "grep" not in line:
            listin.append(line.rstrip('\n').split(' '))


#gatherInfo generates some nasty stuff so this gets rid of that crap.
def removeEmpty(listin):
    i = 0
    while i < len(listin):
        if listin[i] == '':
            del listin[i]
            i = 0
        i += 1
    return listin

#Goes through the stuff gatherInfo spits out and adds it to the list that given as a parameter.
def triageProcesses(listin):
    for process in processes:
        process = removeEmpty(process)
        if process[1] in protected:
            pass
        else:
            listin.append(process[1])

#Kill all processes in its list and them emptys the list so it doesnt try and kill non-existing processes.
def killProcesses():
    for process in tokill:
        os.system("sudo kill " + process)
    del tokill[:]
             
#Protect the intialy connected connections.
gatherInfo(processes)
triageProcesses(protected)


#Close all other connections forever.
while True:
    gatherInfo(processes)
    triageProcesses(tokill)
    killProcesses()
    time.sleep(.5)