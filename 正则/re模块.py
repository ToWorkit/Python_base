# 字符串
# 对应的正则表达式字符串会变为 'ABC\-000'
s = 'ABC\\-000'
print(s)
# 使用python的 r 前缀，就避免转义的问题
# r 防止字符串转义
s2 = r'PL\-LP' 
print(s2)

# 判断正则表达式是否匹配
import re
re.match(r'\d{3}\-\d{3,8}$', '019-19823')
# math()
# 判断是否匹配
# 成功返回一个Match对象
# 失败返回None
print(re.match(r'^\d{3}\s\d{3,8}$', '000 12345'))
'''
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
'''

# 切分字符串
_str = 'ab  c'
print(_str.split(' '))
# 识别空格
print(re.split(r'\s+', 'a   b, c'))
# 识别逗号
print(re.split(r'[\s\,]+', 'a, b  , c'))
# 识别分号
print(re.split(r'[\s\,\;]+', 'a;b;,c,'))
