f = open('test_02.txt', 'r', encoding = 'utf8')
# 打印光标
print(f.tell())
# 打印十个字符 一个中文占三个字符
print(f.read(2))
print(f.tell())
# 调整光标位置 按字符调整
# 可以用来做断点续传的操作
f.seek(6)
print(f.read())
f.close()
