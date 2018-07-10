import itertools

# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
#
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

# ns = itertools.repeat('A',3)
# for n in ns:
#     print(n)

# taskwhile()可用来截取有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10,natuals)
print(list(ns))


