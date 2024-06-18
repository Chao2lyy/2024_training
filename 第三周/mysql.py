from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# 创建数据库引擎
engine = create_engine('mysql+pymysql://root:root@192.168.110.88:3306/ht-atp')

# 创建表，获取会话
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# 增加数据
user1 = User(name='xiaoming', age=25)
session.add(user1)
session.commit()

# 查询数据
user = session.query(User).filter_by(name='xiaoming').first()
print(f"查询到的用户: {user.name}, {user.age}")

# 更新数据
user.age = 26
session.commit()

# 删除数据
session.delete(user)
session.commit()

# 关闭会话
session.close()