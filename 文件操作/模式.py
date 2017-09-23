# r+ 读写模式
# w+ 写读模式
# a+ 追加读模式

# r+
f = open('test.txt', 'r+', encoding='utf8')
print(f.readline()) # 读取行
f.write('Hello World\n') # 写
f.close()
