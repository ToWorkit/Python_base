l = ['Hello', 'World', 'You', 'Ok']
print([item.lower() for item in l])
# 跳过不能操作的整数项
# 非字符串类型没有lower() 方法
l_02 = ['Hello', 'World', 20, 'You', 'Ok', [2], {3}, 'NICE']
# 处理类型是字符串的
print([item.lower() for item in l_02 if isinstance(item, str) ])
