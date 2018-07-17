from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 把关系数据库的表结构映射到对象上
Base = declarative_base()

# 定义User对象（一张表定义一个对象）
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))

# 初始化连接数据库
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 我们向数据库表中添加一行记录，可以视为添加一个User对象

session = DBSession()
new_user = User(id='5', name='Bob')
session.add(new_user)
session.commit()
session.close()