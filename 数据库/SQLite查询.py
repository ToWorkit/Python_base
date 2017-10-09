# 使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。
# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
# 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
import sqlite3
conn = sqlite3.connect('test_sqlite.db')
cursor = conn.cursor()
# 执行查询语句
# tuple 格式一个数据后面加 ,
cursor.execute('select * from user where id=?', ('1',))
# 获得查询结果
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
