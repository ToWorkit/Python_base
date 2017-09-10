l = ['adam', 'LISA', 'barT']
def fac(x):
  return x.capitalize()
print(list(map(fac, l)))
# str = "www.runoob.com"
# print(str.upper())          # 把所有字符中的小写字母转换成大写字母
# print(str.lower())          # 把所有字符中的大写字母转换成小写字母
# print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
# print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写 

def char(s):
  return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print({'0': 0, '1': 1}['1'])
print(list(map(char, '13579')))
