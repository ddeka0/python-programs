#!/usr/bin/python

f = open("file1.txt",'r')
sum = 0
for line in f:
  wordlist = line.split()
  for word in wordlist:
    number = int(word)
    sum += number
print "The sum is: ",sum

