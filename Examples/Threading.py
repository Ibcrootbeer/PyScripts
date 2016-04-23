#!/usr/bin/env python

import thread
import os

print 'ehllo'

def printit(item):
    os.system(item)

try:
    thread.start_new_thread(printit, ("ls",))
    thread.start_new_thread(printit, ("pwd",))
    thread.start_new_thread(printit, ("gnome-terminal -e ls",))
except:
    print "Fucked"
    
while 1:
    pass