f = open('test_02.txt', 'r', encoding = 'utf8')
# print(f.readline())
# print(f.readline())
# 列表格式列表
# print(f.readlines())
cor = 0
for i in f.readlines():
  cor += 1
  if cor == 6:
    # i = i.strip() + ' <----'
    # 字符串拼接用join
    # 默认删除空白符 strip
    i = ''.join([i.strip(), ' -----'])
  # 去掉换行符
  print(i.strip())
f.close()
