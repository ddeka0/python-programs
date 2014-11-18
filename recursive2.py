#!/usr/bin/python

def sum(lower,upper):
    print lower," ",upper
    if lower > upper:
      print 0
      return 0
    else:
      result = lower + sum(lower+1,upper)
      print result
      return result

def main():
    a = input("Enter a lower number: ")
    b = input("Enter a upper number: ")
    c = sum(a,b)
    print "The result is: ",c

main()

