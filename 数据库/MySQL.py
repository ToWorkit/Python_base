# 导入MySQL驱动
import mysql.connector
# 连接信息,test数据库
conn = mysql.connector.connect(user='root', password='12345678', database='test')
cursor = conn.cursor()
# 创建user表
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，mysql中的占位符是 %s
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'PL'])
# 显示插入的行数
print(cursor.rowcount)
# 提交操作
conn.commit()
cursor.close()
conn.close()
