# -*- coding: utf-8 -*-
from functools import reduce
def normalize(name):
	name = name[0].upper()+name[1:].lower()
	return name

def produce(L):
	return reduce(lambda x, y: x*y, L)