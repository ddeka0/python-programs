#!/usr/bin/python

filename = raw_input("Enter the file name: ")
f = open(filename,'r')


numbers = []
for line in f:
  words = line.split()
  for word in words:
    numbers.append(float(word))


numbers.sort()
print "Last number after sorting is:",numbers[-1]
midpoint = len(numbers)/2
print "The median is:",
if len(numbers) % 2 == 1:
  print numbers[midpoint]
else:
  print (numbers[midpoint] + numbers[midpoint-1]) / 2.0

f.close() 
