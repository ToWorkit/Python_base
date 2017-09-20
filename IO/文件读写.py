# 标识符 r 表示读, 指定编码
f = open('test.txt', 'r', encoding='utf8')
print(f.read())
for line in f.readlines():
  print(line.strip())
# 文件使用完毕后必须关闭
f.close()
# 尽量使用 try...finally 来处理文件读写
# 不管文件是否正确的读写都必须能正确的关闭文件
try:
  f = open('test.txt', 'r')
  print(f.read())
finally:
  if f:
    f.close()  

# 使用 with 语句自动调用 close() 方法
with open('test.txt', 'r') as f:
  print(f.read())

# 二进制文件
img = open('1.png', 'rb')
print(img.read())

# 字符编码
t = open('test_02.txt', 'r', encoding = 'utf-8', errors='ignore') # 直接忽略UnicodeDecodeError
t = open('test_02.txt', 'r', encoding = 'utf-8')
print(t.read())

# 写文件
w = open('test.txt', 'w')
w.write('Hello LP')
# 写文件时必须有close
w.close()
# 读写操作尽量使用 with 也可以使用encoding
with open('test.txt', 'w') as W:
  W.write('Hello PL')
