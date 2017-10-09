# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320114981139589ac5f02944601ae22834e9c521415000
# 导入
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()
# 定义User对象
class User(Base):
  # 表的名字
  __tablename__ = 'user'
  # 表结构
  id = Column(String(20), primary_key=True)
  name = Column(String(20))
# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:12345678@localhost:3306/test')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()
# 创建新User对象
new_user = User(id='2', name='LP')
# 添加到session
session.add(new_user)
# 提交操作数据库
session.commit()
# 关闭session
session.close()
