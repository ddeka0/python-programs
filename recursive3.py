#!/usr/bin/python

List = []

def display(lower,upper):
    print lower,"  ",List
    if lower > upper:
      return "end"
    else:
      display(lower+1,upper)
      List.append(lower)
      #print List

def main():
    a = input("Enter lower bound integer: ")
    b = input("Enter upper bound integer: ")
    display(a,b)

main()

