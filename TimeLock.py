#!/usr/bin/env python

import hashlib
import datetime
import time
import sys

alpha = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'

def getCode(md5):
    alphastr = ''
    numstr = ''
    alphanum = 0
    numnum = 0
    for i in md5:
        if i in alpha:
            if alphanum < 2:
                alphastr += i
                alphanum += 1
    for i in reversed(md5):
        if i in num:
            if numnum < 2:
                numstr += i
                numnum += 1
    return alphastr + numstr

def getTimeLockTime(time):
    return int((time + (60 -(time % 60))) - 60)

def getMD5(string):
    return hashlib.md5(hashlib.md5(str(string)).hexdigest()).hexdigest()

def generateCode(epoch, current):
    epoch = convertToUTC(epoch)
    current = convertToUTC(current)
    seconds = int((current - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = getCode(md5)
    return code

def currentCode():
    return generateCode(datetime.datetime.fromtimestamp(0), datetime.datetime.now())
    
def convertToUTC(date):
    return date.utcfromtimestamp(time.mktime(date.timetuple()))
    
def printDetails():
    epoch = datetime.datetime.fromtimestamp(0)
    current = datetime.datetime.now()
    #Just to get rid of the miliseconds from now() output
    current = datetime.datetime(current.year, current.month, current.day, current.hour, current.minute, current.second)
    seconds = int((current - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = getCode(md5)
    
    utcepoch = convertToUTC(epoch)
    utccurrent = convertToUTC(current)
    utcseconds = int((utccurrent - utcepoch).total_seconds())
    utctimeLockTime = str(getTimeLockTime(utcseconds))
    utcmd5 = getMD5(utctimeLockTime)
    utccode = getCode(utcmd5)
    
    print "Epoch:\t\t" + str(epoch) + '\t\t\tUTC: ' + str(utcepoch)
    print "Current:\t" + str(current) + '\t\t\tUTC: ' + str(utccurrent)
    print "Seconds:\t" + str(seconds) + '\t\t\t\tUTC: ' + str(utcseconds)
    print "TLT:\t\t" + timeLockTime + '\t\t\t\tUTC: ' + utctimeLockTime
    print "MD5:\t\t" + md5 + '\tUTC: ' + utcmd5
    print "Code:\t\t" + code + '\t\t\t\t\tUTC: ' + utccode
    print "generateCodeOutput: " + generateCode(epoch, current)
    
def printDetailsInput(epoch, current):
    seconds = int((current - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = getCode(md5)
    
    utcepoch = convertToUTC(epoch)
    utccurrent = convertToUTC(current)
    utcseconds = int((utccurrent - utcepoch).total_seconds())
    utctimeLockTime = str(getTimeLockTime(utcseconds))
    utcmd5 = getMD5(utctimeLockTime)
    utccode = getCode(utcmd5)
    
    print "Epoch:\t\t" + str(epoch) + '\t\t\tUTC: ' + str(utcepoch)
    print "Current:\t" + str(current) + '\t\t\tUTC: ' + str(utccurrent)
    print "Seconds:\t" + str(seconds) + '\t\t\t\tUTC: ' + str(utcseconds)
    print "TLT:\t\t" + timeLockTime + '\t\t\t\tUTC: ' + utctimeLockTime
    print "MD5:\t\t" + md5 + '\tUTC: ' + utcmd5
    print "Code:\t\t" + code + '\t\t\t\t\tUTC: ' + utccode
    print "generateCodeOutput: " + generateCode(epoch, current)
    
printDetailsInput(datetime.datetime(1999, 12, 31, 23, 59, 59), datetime.datetime(2000, 1, 1, 0, 0, 59))

print

printDetails()

'''
try:
    if sys.argv[1] == "-test":
        printDetailsInput(datetime.datetime(1999, 12, 31, 32, 59, 59), datetime.datetime(2000, 01, 01, 0, 0, 59))
except:
    print currentCode()
'''