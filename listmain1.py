#!/usr/bin/python

from listclass1 import Node

head = None
curr = None
b = 1
for count in xrange(1,6):
  if head != None:
    curr = head
    print curr.next
    while curr.next != None:
      print b
      curr = curr.next
      b += 1
   
    #curr = curr.next
    curr = Node(count)
    b = 1
  else:
    print "First Time "
    head = Node(count)
    #curr = head
    #print curr.data," .and. ",curr.next

if head != None:
  #print "Head is not None"
  curr = head
  #print curr.data
  while curr != None:
    curr = curr.next
    #print "ghghg"
