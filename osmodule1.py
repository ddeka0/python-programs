#!/usr/bin/python

import os
count = 0
currentrdirectorypath = os.getcwd()
listoffilenames = os.listdir(currentrdirectorypath)
print "%10s%20s" % ("file No.","names")
for names in listoffilenames:
  fragmentedname = names.split(".")  #now fragmentedname is a list containing two member
  if fragmentedname[-1] == "py":
    count += 1
    print "%10d%20s" % (count,names)

