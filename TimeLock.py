#!/usr/bin/env python

import calendar
import time
import hashlib
import sys
import datetime
from datetime import tzinfo, timedelta

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

def debugPrint():
    print "Current Time: \t" + str(time)
    print "Time Lock Time: " + str(getTimeLockTime(time))
    print "MD5: \t\t" + md5
    print "Code: \t\t" + getCode(md5)
    
def challengeCode():
    epoch = datetime.datetime(2016, 01, 01, 00, 00, 00)
    current =  datetime.datetime.now()
    seconds = int((current - epoch).total_seconds())
    tlt = getTimeLockTime(seconds)
    md5 = getMD5(tlt - 60)
    code = getCode(md5)
    
    print code
    print getCode(getMD5(tlt - 3600 - 60)) + "   dls"

#begins at 2:00 a.m. on the second Sunday of March and
#ends at 2:00 a.m. on the first Sunday of November
def first_sunday_on_or_after(dt):
    days_to_go = 6 - dt.weekday()
    if days_to_go:
        dt += timedelta(days_to_go)
    return dt
    
def debugCode():
    print "Epoch\t\t\tCurrent\t\t\tSeconds\t\tTLT\t\tMD5\t\t\t\t\tCode\tTarget"
    epoch = datetime.datetime(1999, 12, 31, 23, 59, 59)
    currentTime = datetime.datetime(2013, 05, 06, 07, 43, 25)
    seconds = int((currentTime - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = getCode(md5)
    print str(epoch) + "\t" + str(currentTime) + '\t' + str(seconds) + '\t' + timeLockTime + '\t' + str(md5) + '\t' + code + '\t' + "ca63"
    
    epoch = datetime.datetime(2001, 02, 03, 04, 05, 06)
    currentTime = datetime.datetime(2010, 06, 13, 12, 55, 34)
    seconds = int((currentTime - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = getCode(md5)
    print str(epoch) + "\t" + str(currentTime) + '\t' + str(seconds) + '\t' + timeLockTime + '\t' + str(md5) + '\t' + code + '\t' + "dd15" + '\t' + "dlst"
    
    epoch = datetime.datetime(2015, 01, 01, 00, 00, 00)
    currentTime = datetime.datetime(2015, 05, 15, 14, 00, 00)
    seconds = int((currentTime - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = getCode(md5)
    print str(epoch) + "\t" + str(currentTime) + '\t' + str(seconds) + '\t' + timeLockTime + '\t' + str(md5) + '\t' + code + '\t' + "ba26" + '\t' + "dlst"
    
    epoch = datetime.datetime(2014, 12, 31, 00, 00, 00)
    currentTime = datetime.datetime(2015, 01, 01, 00, 00, 00)
    seconds = int((currentTime - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = getCode(md5)
    print str(epoch) + "\t" + str(currentTime) + '\t' + str(seconds) + '\t\t' + timeLockTime + '\t\t' + str(md5) + '\t' + code + '\t' + "dc24"
    
    epoch = datetime.datetime(2014, 12, 31, 00, 00, 00)
    currentTime = datetime.datetime(2015, 01, 01, 00, 00, 30)
    seconds = int((currentTime - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = getCode(md5)
    print str(epoch) + "\t" + str(currentTime) + '\t' + str(seconds) + '\t\t' + timeLockTime + '\t\t' + str(md5) + '\t' + code + '\t' + "dc24"
    
    epoch = datetime.datetime(2014, 12, 31, 00, 00, 00)
    currentTime = datetime.datetime(2015, 01, 01, 00, 01, 00)
    seconds = int((currentTime - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = getCode(md5)
    print str(epoch) + "\t" + str(currentTime) + '\t' + str(seconds) + '\t\t' + timeLockTime + '\t\t' + str(md5) + '\t' + code + '\t' + "ec29"
    
    epoch = datetime.datetime(2014, 12, 31, 00, 00, 00)
    currentTime = datetime.datetime(2015, 01, 01, 00, 01, 30)
    seconds = int((currentTime - epoch).total_seconds())
    timeLockTime = str(getTimeLockTime(seconds))
    md5 = getMD5(timeLockTime)
    code = getCode(md5)
    print str(epoch) + "\t" + str(currentTime) + '\t' + str(seconds) + '\t\t' + timeLockTime + '\t\t' + str(md5) + '\t' + code + '\t' + "ec29"

now = calendar.timegm(time.gmtime())
md5 = getMD5(str(getTimeLockTime(now)))


currentTime = datetime.datetime(2010, 06, 13, 12, 55, 34)

debugCode()


#challengeCode()

'''
try:
    if sys.argv[1] == "-test":
        debugCode()
        #debugPrint()
except:
    print getCode(md5)
'''