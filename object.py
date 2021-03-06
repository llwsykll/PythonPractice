# -*- coding: utf-8 -*-
from enum import  Enum,unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
	count = 0;
	def __init__(self,name,score,gender):
		self.__name = name
		self.__score = score
		self.gender = gender
		Student.count+=1

	def print_score(self):
		print('%s: %s' % (self.__name,self.__score))

	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'

	def set_score(self,score):
		if 0<=score<=100:
			self.__score = score
		else:
			raise ValueError('bad score')

	def get_gender(self):
		print('%s: %s' % (self.__name,self.__gender))

	def set_gender(self,gender):
		if gender=='male' or gender=='female':
			self.__gender = gender
		else:
			raise ValueError('bad gender')
