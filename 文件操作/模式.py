# r+ 读写模式
# w+ 写读模式
# a+ 追加读模式

# r+
'''
f = open('test.txt', 'r+', encoding='utf8')
print(f.readline()) # 读取行
f.seek(0)
f.write('123 World\n') # 写
# 查看光标位置
# 大写字母占三个字符，小写占一个
print(f.tell())
f.close()
'''
# a+
# f = open('test.txt', 'a+', encoding='utf8')
# # 因为追加的光标会在末尾，所以没有数据可读
# print(f.readline())
# print(f.tell())
