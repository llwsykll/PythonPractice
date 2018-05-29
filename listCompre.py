# -*- coding: utf-8 -*-
def listCompre(L):
	S=[s.lower() for s in L if isinstance(s,str)]
	print(S)