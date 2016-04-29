#!/usr/bin/env python

#####
#strings for printable characters from file
#####

#The byte method works by replacing every (interval)th byte with the next byte from the file to hide
#How does the bit method work

import sys

def parseCommandLine():
    global interval
    global bit
    global retrieval
    global hidden
    global wrapper
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
        if(i[:2] == "-w"): # set wrapper to file
            wrapper = i[2:]
        if(i[:2] == "-h"): # set hidden file to
            hidden = i[2:]
        counter += 1

def writeToFile(hidden):  
    if(hidden != ''):
        hidden = open(hidden, 'w')

def readByteFromFile(wrapper): #Do backwards as well
    output = ''
    with open(wrapper, 'r') as wrapperFile:
        wrapperFile.read(offset)
        fromFile = wrapperFile.read(1)
        while(fromFile != ''):
            output += fromFile   
            wrapperFile.read(interval - 1)
            fromFile = wrapperFile.read(1)
        return output

def writeByteToFile(fileToHideIn, fileToWrite):
    counter = 0
    with open(fileToHideIn, 'w') as wrapperFile:
        with open(fileToWrite, 'r') as hiddenFile:
            fromFile = hiddenFile.read(1)
            while(fromFile != ''):
                print fromFile
                fromFile = hiddenFile.read(1)  

interval = 0        #Jumps inbetween bytes to read
bit = False         #To use the bit method or not DO FROM BACK TO FRONT
retrieval = False   #To search the wrapper or nots
hidden = ""         #The file to hide within the wrapper
wrapper = ""        #The file containing the hidden data we want to search through
store = False       #To hide the hidden file or not
offset = 0          #Initial jump to bypass header

parseCommandLine()
#print readByteFromFile(wrapper)
writeByteToFile(wrapper, hidden)