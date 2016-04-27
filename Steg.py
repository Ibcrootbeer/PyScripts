#!/usr/bin/env python

#####
#strings for printable characters from file
#####

import sys

def parseCommandLine():
    global interval
    global bit
    global retrieval
    global fileToHide
    global fileToSearch
    global store
    global offset
    
    counter = 0
    while counter < len(sys.argv):
        i = sys.argv[counter]
        if(i[:2] == "-o"):  # set offset to ? 
            offset = int(i[2:])
        if(i[:2] =="-b"): # use the bit method
            bit = True
        if(i[:2] == "-r"): # retrieve hidden data
            retrieval = True
        if(i[:2] == "-B"): # use the byte method
            bit = False
        if(i[:2] == "-s"): # store and hide
            store = True
        if(i[:2] == "-i"): # set interval to file
            interval = int(i[2:])
        if(i[:2] == "-w"): # set fileToSearch to file
            fileToSearch = i[2:]
        if(i[:2] == "-h"): # set hidden file to
            fileToHide = i[2:]
        counter += 1

def writeToFile(fileToHide):  
    if(fileToHide != ''):
        fileToHide = open(fileToHide, 'w')

def readFromFile(fileToSearch): #Do backwards as well
    if(fileToSearch != ''):
        output = ''
        fileToSearch = open(fileToSearch, 'r')
        fromFile = fileToSearch.read(offset)
        fromFile = fileToSearch.read(1)
        while(fromFile != ''):
            if(bit):
                output += '1' if ord(fromFile) & 0x01 else '0'
            else:
                output += fromFile
                
            fileToSearch.read(interval - 1)
            fromFile = fileToSearch.read(1)
        return output

def writeToFile():
    pass

interval = 0        #Jumps inbetween bytes to read
bit = False         #To use the bit method or not DO FROM BACK TO FRONT
retrieval = False   #To search the wrapper or not
fileToHide = ""     #The file to hide within the wrapper
fileToSearch = ""   #The file containing the hidden data we want to search through
store = False       #To hide the hidden file or not
offset = 0          #Initial jump to bypass header

parseCommandLine()
print readFromFile(fileToSearch)