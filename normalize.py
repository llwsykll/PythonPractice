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
   n=s.index('.')
   s1=list(map(int,[x for x in s[:n]]))
   s2=list(map(int,[x for x in s[n+1:]]))
   return reduce(fn,s1) + reduce(fn,s2)/10**len(s2)
