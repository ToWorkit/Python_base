def my_abs (x):
    if not isinstance(x, (int, float)): # 只允许整数和浮点数类型
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 输入的数据会是字符串格式需要转为int整数类型
print(my_abs(int(input('输入数据'))))
