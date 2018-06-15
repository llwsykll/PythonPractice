# -*- coding: utf-8 -*-
from functools import reduce
def normalize(name):
	name = name[0].upper()+name[1:].lower()
	return name

def produce(L):
	return reduce(lambda x, y: x*y, L)

def str2float(s):
   def fn(x, y):
        return x * 10 + y
   def char2num(s):
         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
   return reduce(fn, map(char2num, s.replace(".","")))
