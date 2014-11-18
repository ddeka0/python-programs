#!/usr/bin/python

def displayrange(lower,upper):
    if lower <= upper:
      print lower  ,
      displayrange(lower+1,upper)
    else:
      return 0;

def sum(lower,upper):
    if lower > upper:
      return 0;
    else:
      return lower + sum(lower + 1,upper)


def main():
    a = input("Enter lower bound: ")
    b = input("Enter upper bound: ")
    displayrange(a,b)
    c = sum(a,b)
    print "\nSummation is: =",c

main()
