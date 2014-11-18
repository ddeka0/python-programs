#!/usr/bin/python

import math

area = input("Enter the area: ")
if area>0:
  radius = math.sqrt(area/math.pi)
  print "The radius is",radius
else:
  print "Error: the area must be a positive number"

