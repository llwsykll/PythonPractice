import itertools

def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    nstuals = itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.takewhile(lambda x:x <= 2 * N,nstuals)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    L = list(ns)
    sum = 0
    for l in L:
        if(l%4 != 1):
            l = 0-l
        sum = sum+4/l

    # step 4: 求和:
    return sum

print(pi(10))
print(pi(100))
print(pi(1000))