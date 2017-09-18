# 使用 in 判断 是否在
print('l' in 'Hello World')

# 格式字符串
print('%s love me' % 'LP')

# 字符串拼接
a = 'Hello '
b = 'World'
c = ''.join([a, b])
print(c)

# String 内置方法

# 统计字符个数
print('Hello'.count('l'))

# 字符串放中间左右补充 共20个*
print('World'.center(20, '*'))

# 以什么为开头 结尾, 严格规范大小写 可加范围
print('Hello'.startswith('H'))
print('Hello'.endswith('lo'))

st = 'He\tllo World'
# 配合 \t 使用
print(st.expandtabs(tabsize = 10))
# 查找第一个位置 有则返回位置，无则返回 -1
print(st.find('\t'))

# 字符串格式化的另一种方式
l = 'Hello {name}, love {favour}'
# print(l.format(name = 'Lp', favour = 'pl'))
print(l.format_map({
  'name': 'pp',
  'favour': 'll'
}))
# 位置， 有则返回，无则报错
print(st.index('l'))

# 判断字符串是有否包含数字, 其他字符不行
print('abc123'.isalnum())

# 去掉换行和空格
p = '   Hello    '
print(p)
print(p.strip())

# 替换, 默认替换所有，第三个参数为控制替换次数(深度)
r = 'Hello World'
print(r.replace('World', 'Lp'))

# 字符串分割, 第二个参数为分割深度(次数)
print(r.split(' '))

sp = '?book_id=90&username=pp'
print(sp.split('='))

# 首字母都大写
print('hello world'.title())
