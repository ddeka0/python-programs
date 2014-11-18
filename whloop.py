#!/usr/bin/python

done = False
while not done:
  number = input("Enter marks: ")
  if number >=0 and number <=100:
    done = True
  else:
    print "Error in input"
print number

