#!/usr/bin/python

import os, os.path

QUIT = '7'

COMMANDS = ('1','2','3','4','5','6','7')            # tuple is created

MENU = """ 1 List the current director
 2 Move up
 3 Move down
 4 Number of files in the directory
 5 Size of directory in byte
 6 Search for a filename
 7 quit the program """

def main():
    while True:
      print "\nLOADING ::::::::::  STARTING  :::::::::::::::\n"
      print "Current directory: ",os.getcwd()        # prints the menu and present directory name ::
      print MENU
      command = acceptcommand()
      runcommand(command)
      if command == QUIT:
        print "Have a nice day ! "
        break

def acceptcommand():
    while True:
      command = raw_input("Enter a number: ")
      if not command in COMMANDS:
        print "Error: commands not recognized"
      else:
        return command

def runcommand(command):
    if command == '1':
      listcurrentdir(os.getcwd())
    elif command == '2':
      moveup()
    elif command == '3':
      movedown(os.getcwd())
    elif command == '4':
      print "The total no of files is= ", countfiles(os.getcwd())
    elif command == '5':
      print "The total no of bytes is= ", countbytes(os.getcwd())
    elif command == '6':
      target = raw_input("Enter the search string: ")
      filelist = findfiles(target,os.getcwd())
      if not filelist:
        print "String not found"
      else:
        for f in filelist:
          #print "Found files are: "
          print f

def listcurrentdir(dirname):
    lyst = os.listdir(dirname)
    for element in lyst:
      print element

def moveup():
    os.chdir("..")

def movedown(currentdir):
    newdir = raw_input("Enter the directory name: ")
    if os.path.exists(currentdir + os.sep + newdir) and os.path.isdir(newdir): 
                                                   # cross checking of directory existance
      os.chdir(newdir)
    else:
      print "ERROR: no such name"

def countfiles(path):
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
      if os.path.isfile(element):
        count += 1
      else:
        os.chdir(element)
        count += countfiles(os.getcwd())
        os.chdir("..")                             # return to previous directory :: will work in a recursive way
    return count

def countbytes(path):
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
      if os.path.isfile(element):
        count += os.path.getsize(element)
      else:
        os.chdir(element)
        count == countbytes(os.getcwd())
        os.chdir("..")
    return count

def findfiles(target,path):
    files = []
    lyst = os.listdir(path)
    for element in lyst:
      if os.path.isfile(element):
        if target in element:                      # target and element both are strings now :: so if only a part of filename is entered correctly then also this method
                                                   # will detect the requied files
          files.append(path + os.sep + element)
      else:
        os.chdir(element)
        files.extend(findfiles(target,os.getcwd()))
        os.chdir("..")
    return files

main()
