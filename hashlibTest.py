#常见的摘要算法（MD4，SHA1等）摘要算法又称哈希算法、散列算法。
# 它通过一个函数
# 把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）

import hashlib

# md5速度很快，生成结果固定128bit
md5 = hashlib.md5()
md5.update('chenqiuyuan is a pig.'.encode('utf-8'))
print(md5.hexdigest())


md5.update('chenqiuyuan'.encode('utf-8'))
md5.update(' is a pig.'.encode('utf-8'))
print(md5.hexdigest())

# sha1 结果是160bit
sha1 = hashlib.sha1()
sha1.update('chenqiuyuan is a pig.'.encode('utf-8'))
print(sha1.hexdigest())

sha1.update('chenqiuyuan'.encode('utf-8'))
sha1.update(' is a pig.'.encode('utf-8'))
print(sha1.hexdigest())

