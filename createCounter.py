# -*- coding: utf-8 -*-
def createCounter():
	n = 0
	def counter():
		nonlocal n              #必须加nonlocal
		n=n+1
		return n
	return counter