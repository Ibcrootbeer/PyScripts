#!/usr/bin/env python

import hashlib
import datetime
import sys
import calendar
import time

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
    seconds = int((current - epoch).total_seconds())
    if isDayLightSavingsTime(epoch) != isDayLightSavingsTime(current): 
        seconds -= 3600
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = getCode(md5)
    return code
    

#begins at 2:00 a.m. on the second Sunday of March and
#ends at 2:00 a.m. on the first Sunday of November
def isDayLightSavingsTime(date):
    if date.month < 3 or date.month > 11:
        return False
    if date.month > 3 and date.month < 11:
        return True
    counter = 1
    sundayCounter = 0
    marchDate = datetime.datetime(date.year, 3, 1, 2, 0 ,0)
    #Sets the marchDate to the 2nd sunday in march at 2AM
    while marchDate.strftime("%A") != 'Sunday' or sundayCounter < 2:
        marchDate = datetime.datetime(date.year, 3, counter, 2, 0 ,0)
        if marchDate.strftime("%A")  == 'Sunday':
            sundayCounter += 1
        counter += 1
    
    counter = 1
    novemberDate = datetime.datetime(date.year, 11, 1, 2, 0 ,0)
    #Sets novemberDate to the first sunday in november at 2AM
    while novemberDate.strftime("%A") != 'Sunday':
        novemberDate = datetime.datetime(date.year, 11, counter, 2, 0 ,0)
        counter += 1
    
    if date < novemberDate and date > marchDate:
        return True
    else:
        return False
    
def debugCode():
    print "Epoch\t\t     isDLST\tCurrent\t\t     isDLST\tSeconds\t\tTLT\t\tMD5\t\t\t\t\tCode\tTarget"
    epoch = datetime.datetime(1999, 12, 31, 23, 59, 59)
    currentTime = datetime.datetime(2013, 05, 06, 07, 43, 25)
    seconds = int((currentTime - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = generateCode(epoch, currentTime)
    print str(epoch) + ", " + str(isDayLightSavingsTime(epoch)) + '\t' + str(currentTime) + ', ' + str(isDayLightSavingsTime(currentTime)) + '\t' + str(seconds) + '\t' + timeLockTime + '\t' + str(md5) + '\t' + code + '\t' + "ca63"
    
    epoch = datetime.datetime(2001, 02, 03, 04, 05, 06)
    currentTime = datetime.datetime(2010, 06, 13, 12, 55, 34)
    seconds = int((currentTime - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = generateCode(epoch, currentTime)
    print str(epoch) + ", " + str(isDayLightSavingsTime(epoch)) + '\t' + str(currentTime) + ', ' + str(isDayLightSavingsTime(currentTime)) + '\t' + str(seconds) + '\t' + timeLockTime + '\t' + str(md5) + '\t' + code + '\t' + "dd15" + '\t' + "dlst"
    
    epoch = datetime.datetime(2015, 01, 01, 00, 00, 00)
    currentTime = datetime.datetime(2015, 05, 15, 14, 00, 00)
    seconds = int((currentTime - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = generateCode(epoch, currentTime)
    print str(epoch) + ", " + str(isDayLightSavingsTime(epoch)) + '\t' + str(currentTime) + ', ' + str(isDayLightSavingsTime(currentTime)) + '\t' + str(seconds) + '\t' + timeLockTime + '\t' + str(md5) + '\t' + code + '\t' + "ba26" + '\t' + "dlst"
    
    epoch = datetime.datetime(2014, 12, 31, 00, 00, 00)
    currentTime = datetime.datetime(2015, 01, 01, 00, 00, 00)
    seconds = int((currentTime - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = generateCode(epoch, currentTime)
    print str(epoch) + ", " + str(isDayLightSavingsTime(epoch)) + '\t' + str(currentTime) + ', ' + str(isDayLightSavingsTime(currentTime)) + '\t' + str(seconds) + '\t\t' + timeLockTime + '\t\t' + str(md5) + '\t' + code + '\t' + "dc24"
    
    epoch = datetime.datetime(2014, 12, 31, 00, 00, 00)
    currentTime = datetime.datetime(2015, 01, 01, 00, 00, 30)
    seconds = int((currentTime - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = generateCode(epoch, currentTime)
    print str(epoch) + ", " + str(isDayLightSavingsTime(epoch)) + '\t' + str(currentTime) + ', ' + str(isDayLightSavingsTime(currentTime)) + '\t' + str(seconds) + '\t\t' + timeLockTime + '\t\t' + str(md5) + '\t' + code + '\t' + "dc24"
    
    epoch = datetime.datetime(2014, 12, 31, 00, 00, 00)
    currentTime = datetime.datetime(2015, 01, 01, 00, 01, 00)
    seconds = int((currentTime - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = generateCode(epoch, currentTime)
    print str(epoch) + ", " + str(isDayLightSavingsTime(epoch)) + '\t' + str(currentTime) + ', ' + str(isDayLightSavingsTime(currentTime)) + '\t' + str(seconds) + '\t\t' + timeLockTime + '\t\t' + str(md5) + '\t' + code + '\t' + "ec29"
    
    epoch = datetime.datetime(2014, 12, 31, 00, 00, 00)
    currentTime = datetime.datetime(2015, 01, 01, 00, 01, 30)
    seconds = int((currentTime - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = generateCode(epoch, currentTime)
    print str(epoch) + ", " + str(isDayLightSavingsTime(epoch)) + '\t' + str(currentTime) + ', ' + str(isDayLightSavingsTime(currentTime)) + '\t' + str(seconds) + '\t\t' + timeLockTime + '\t\t' + str(md5) + '\t' + code + '\t' + "ec29"


now = calendar.timegm(time.gmtime())
md5 = getMD5(str(getTimeLockTime(now)))

try:
    if sys.argv[1] == "-test":
        debugCode()
except:
    print getCode(md5)