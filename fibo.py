#!/usr/bin/python

def fib(n):
    if n < 3:
      return 1
    else:
      return fib(n-1) + fib(n-2)

def main():
    a = input("Enter an integer: ")
    for i in xrange(1,a + 1):
     
        print fib(i)

main()

