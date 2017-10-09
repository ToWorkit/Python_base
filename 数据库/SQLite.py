# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432010494717e1db78cd172e4d52b853e7fd38d6985c000

# 导入SQLite驱动
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test_sqlite.db， 没有会自动在当前目录创建
conn = sqlite3.connect('test_sqlite.db')
# 创建一个Cursor
cursor = conn.cursor()
  # 执行一条SQL语句，创建user表, 执行一次就好
  # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行SQL语句，插入一条记录
cursor.execute('insert into user (id, name) values (\'1\', \'LP\')')
# 通过rowcount获得掺入的行数
print(cursor.rowcount)
# 关闭Cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭Connection
conn.close()
