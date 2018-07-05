# -*- coding: utf-8 -*-

from io import StringIO

f = StringIO()
f.write('lalalalalal')

f.write('陈秋远是猪')

print(f.getvalue())

s = StringIO('陈秋远是猪\n李承阳是小宝贝')
while True:
    str = s.readline()
    if str == '':
        break
    print(str.strip())
