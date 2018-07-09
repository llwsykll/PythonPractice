# struct模块将bytes和其他二进制数据类型转换

import struct

# >I：>表示震惊顺序是网络序，I表示4字节无符号整数
print(struct.pack('>I',10240099))

# >IH：bytes依次变为I：4字节无符号整数  H：2字节无符号整数
print(struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80'))

# 具体定义数据类型参考https://docs.python.org/3/library/struct.html#format-characters

