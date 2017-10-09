import mysql.connector
conn = mysql.connector.connect(user='root', password='12345678', database='test')
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
