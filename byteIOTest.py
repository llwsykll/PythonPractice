# -*- coding:utf-8 -*-

from io import BytesIO
f = BytesIO()
f.write('陈秋远小猪猪'.encode('utf-8'))

print(f.getvalue())

s = BytesIO(b'\xe9\x99\x88\xe7\xa7\x8b\xe8\xbf\x9c\xe5\xb0\x8f\xe7\x8c\xaa\xe7\x8c\xaa')
print(s.read())