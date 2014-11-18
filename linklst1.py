#!/usr/bin/python

from node1 import Node

def main():
	head = None
	for count in xrange(1,6):
  	  head = Node(count,head)

	while head != None:
  	  print head.data
  	  head = head.next

main()
