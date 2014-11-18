#!/usr/bin/python

import random
f = open("integer.txt",'w')
for count in xrange(500):
  number = random.randint(1,500)
  f.write(str(number) + "\n")
f.close()

