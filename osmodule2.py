#!/usr/bin/python


# a program for terminal based directory navigation application written in python......

import os, os.path

QUIT = '7'

COMMANDS = ('1','2','3','4','5','6','7')

MENU = """ 1 List the current directory
           2 Move up
           3 Move down
           4 Number of files in the directory
           5 Size of directory in byte
           6 Search for a filename
           7 quit the program """

def main():
    while True:
      print os.getcwd()
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
      print "The total no of files is", countfiles(os.getcwd())
    elif command == '5':
      print "The total no of bytes is", countbytes(os.getcwd())
    elif command == '6':
      target = raw_input("Enter the search string: ")
      filelist = findfiles(target,os.getcwd())
      if not filelist:
        print "String not found"
      else:
        for f in filelist:
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
        os.chdir("..")
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
        if target in element:
          files.append(path + os.sep + element)
      else:
        os.chdir(element)
        files.extend(findfiles(target,os.getcwd()))
        os.chdir("..")
    return files

main()
