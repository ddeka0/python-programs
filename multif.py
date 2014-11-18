#!/usr/bin/python

number = input("Enter te numeric grade: ")
if number >=0 and number <=100:
  if number>89:
    letter = "A"
  elif number>79:
    letter = 'B'
  elif number>69:
    letter = 'C'
  else:
    letter = 'F'
  print "grade is",letter
else:
  print"Enter: grade must be between 100 and 0"

