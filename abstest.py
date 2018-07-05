# -*- coding: utf-8 -*-
import poolTest
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

s = input('请输入数字:')
a = int(s)
print(my_abs(a))