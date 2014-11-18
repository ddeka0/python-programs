#!/usr/bin/python

class Lcation(object):

	def __init__(self,x,y):
		
		self.x = x
		self.y = y

	def move(self,deltax,deltay):
		return Location(self.x + deltax,self.y + deltay)

	def getx(self):
		return self.x

	def gety(self):
		return self.y

	def distfrom(self,other):
		ox = other.x
		oy = other.y
		xdist = self.x - ox
		ydist = self.y - oy
		return (xdist**2 + ydist**2)**0.5

	def __str__(self):
		return '<' + str(self.x) + ', ' + str(self.y) + '>'


class field(object):

	def __init__():
		self.drunks = {}

	def addrunk(self,drunk,loc):
		if drunk in self.drunk:
			raise ValueError('Duplicate drunk')
		else:
			self.drunks[drunk] = loc
		

		







