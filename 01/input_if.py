# 输入的为字符串str格式，需要转为int格式相比较
birth = int(input('birth: '))
if birth < 2000:
    print('00前')
else:
    print('00后')