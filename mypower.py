# -*- coding: utf-8 -*-
def power(x):
	return x*x

def powern(x,n):
	s = 1
	while n>0:
		n = n - 1
		s = s * x
	return s