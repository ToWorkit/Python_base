# 尽量使用 with 语句操作文件
with open('test.txt', 'r') as r, open('test_02.txt', 'w') as w:
  
# 修改并重新写入新的文件中
r = open('一行一行的读出来.txt', 'r', encoding='utf8')
w = open('再写入新文件内修改.txt', 'w', encoding='utf8')

num = 0
for i in r:
  num += 1
  if num == 3:
    r_list = list(i)
    r_list[r_list.index('明')] = '沧'
    r_list[r_list.index('月')] = '桑'
    i = ''.join(r_list)
  w.write(i)
r.close()
w.close()    
