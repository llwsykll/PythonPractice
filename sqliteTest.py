# 导入SQLite驱动

import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个cursor
cursor = conn.cursor()
# sql语句创建表user
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一条记录
# cursor.execute('insert into user (id, name) values (\'1\',\'LCY\')')

# 查询记录
cursor.execute('select * from user where id=?',('1',))
values = cursor.fetchall()
print(values)

# 查询插入条数
# print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()