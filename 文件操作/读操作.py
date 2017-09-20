# 打开
# 操作
# 关闭
f = open('test.txt', 'r', encoding = 'utf8')

data = f.read(5) # 只显示5个字符
print(data)

f.close()

# 会全自动去关闭
with open('test.txt', 'r', encoding='utf-8') as f:
  print(f.read())
