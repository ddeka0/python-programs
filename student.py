#!/usr/bin/python

from stu import Student


def main():
    
    s = Student("Maria", 5)
    marks = input("Enter any marks: ")
    s.setscore(1,marks)
    #setscore(s,2,marks)    #this is wrong
    #a = s.getscore(1)
    print "Name: ",s.getname(),"\nScore in 1: ",s.getscore(1),"\n"
    print s.__str__()  # same as below
    print str(s)       # same as above
main() 
