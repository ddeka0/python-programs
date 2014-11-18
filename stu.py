#!/usr/bin/python

class Student(object):
    
    def __init__(self,name,number):
        self._name = name
        self._score = []
        for count in xrange(number):
          self._score.append(0)

    def getname(self):
        return self._name

    def setscore(self,i,score):
        self._score[i - 1] = score

    def getscore(self,i):
        return self._score[i - 1]

    def getaverage(self):
        sum = reduce(lambda x, y: x + y,self._score)
        return sum/len(self._score)
  
    def gethighscore(self):
        return max(self._score)

    def __str__(self):
        return "Name: " + self._name + "\nScore: " + "--".join(map(str,self._score))
