from  collections import namedtuple,deque,defaultdict,OrderedDict,Counter

# namedtuple：可自定义的tuple，可根据属性来索引
Point = namedtuple('Point', ['x','y'])
p = Point(1,2)

print(p.x,p.y)

Circle = namedtuple('Circle',['x','y','r'])

# deque：双向列表，可高速插入和删除元素
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict: 索引key不存在是返回默认值
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# OrderedDict: Key按照插入顺序排序
od = OrderedDict([('a',1),('b',2),('c',3)])
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od)

# 使用OrderedDict实现先进先出dict
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdateOrderedDict,self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last = False)
            print('remove:',last)
        if containsKey:
            del self[key]
            print('set:',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key,value)


# Counter: 简单的计数器
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)