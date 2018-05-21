# -*- coding: utf-8 -*-
def findMinAndMax(L):
	if L==[]:
		return(None,None)
	minn = L[0]
	maxz = L[0]
	for i in L:
		if i < minn:
			minn = i
		elif i > maxz:
			maxz = i
	print(minn,maxz)