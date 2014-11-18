#!/usr/bin/python

def main():
    number = input("Enter a number: ")
    result = square(number)
    print "The square of",number,"is =",result

def square(x):
    return x * x

main()


