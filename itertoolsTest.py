import itertools

# 打印自然数序列
natuals = itertools.count(1,2)
for n in natuals:
    print(n)
#
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

# ns = itertools.repeat('A',3)
# for n in ns:
#     print(n)

# taskwhile()可用来截取有限的序列
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x:x<=10,natuals)
# print(list(ns))

# chain: 把一组迭代对象串起来，形成一个更大的迭代器
# for c in itertools.chain('ABC','XYZ'):
#     print(c)
#
# # 将迭代器中相邻重复元素挑出来放在一起
# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key,list(group))
