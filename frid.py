#!/usr/bin/python

f = open("nfile.txt",'r')
while True:
  line = f.readline()
  if line == "":
    break
  print line

