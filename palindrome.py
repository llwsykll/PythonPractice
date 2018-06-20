# -*- coding: utf-8 -*-
def _odd_iter():
	n = 1
	while True:
		n = n + 1
		yield n

def is_palindrome(n):
	nn = str(n)
	return nn == nn[::-1]
