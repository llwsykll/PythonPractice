# -*- coding: utf-8 -*-
def trim(string):
	length = len(string)
	for i in range(length):
		if string[i] == ' ':
			continue
		else:
			break
	j = length - 1
	while string[j] == ' ':
		if j == i:
			break
		j-=1
	new = string[i:j+1]
	print(new)
