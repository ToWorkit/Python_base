# 字符串
# 对应的正则表达式字符串会变为 'ABC\-000'
s = 'ABC\\-000'
print(s)
# 使用python的 r 前缀，就避免转义的问题
# r 防止字符串转义
s2 = r'PL\-LP' 
print(s2)
