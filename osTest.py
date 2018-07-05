# -*- coding:utf-8 -*-

import os
print(os.name)
# print(os.uname())
os.environ
os.environ.get('PATH')
os.environ.get('x','default')

print(os.path.abspath('.'))

print(os.path.join('F:\Python\PythonPractice','testdir'))
# os.mkdir('F:\\Python\\PythonPractice\\testdir')
# os.rmdir('F:\Python\PythonPractice\\testdir')

print(os.path.split('F:\Python\PythonPractice\\factTest.py'))
print(os.path.splitext('F:\Python\PythonPractice\\factTest.py'))

# os.rename('factTest.py','factTest1.py')

[print(x) for x in os.listdir('.') if os.path.isdir(x)]
[print(x) for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']