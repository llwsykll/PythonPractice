# -*- coding: utf-8 -*-
height=1.75
weight=80.5
bmi = 80.5/(1.75*1.75)

if bmi<18.5:
	print('bmi为：',bmi,'过轻')
elif 18.5<bmi<25:
	print('bmi为：',bmi,'正常')
elif 25<bmi<28:
	print('bmi为：',bmi,'过重')
elif 28<bmi<32:
	print('bmi为：',bmi,'肥胖')
else:
	print('bmi为：',bmi,'严重肥胖')