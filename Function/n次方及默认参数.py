# def power(x):
#     return x * x
# print(power(int(input('请输入'))))

# 可设定默认值
# def power(x, n = 2):
#     s = 1
#     while n > 0:
#         n -= 1
#         s *= x
#     return s
# print(power(3))
# print(power(4, 3))

def enroll(name, gender, city = 'BeiJing'):
    print('name ->', name)
    print('city ->', city)
enroll(1, 2, city = 'XiAn')
# 可以不按照顺序，但需要指定键值
enroll(city = 'HangZhou', name = 1, gender = 2)