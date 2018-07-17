import mysql.connector
# 代码与SQLite类似
conn = mysql.connector.connect(user='root',password='123456')
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一条记录
cursor.execute('insert into user (id, name) values (\'1\',\'LCY\')')

print(cursor.rowcount)
conn.commit()
cursor.close()

