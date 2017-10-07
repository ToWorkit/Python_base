# 固定参数， 所以需要将多个参数值作为一个list或tuple传入
def calc(numbers):
    sum = 0
    for num in numbers:
        sum += num * num
    return sum


# 一个参数项
print(calc([1, 2, 3]))  # list
print(calc((1, 3, 5, 7)))  # tuple


# 可变参数 注意 * 号
def calc_02(*numbers):
    sum = 0
    for num in numbers:
        sum += num * num
    return sum


# 多个参数项
print(calc_02(1, 2, 3))

# list或者tuple传入可变参数
list_01 = [1, 2, 3, 4]
print(calc_02(*list_01))
tuple_01 = (1, 3, 5, 7, 8)
print(calc_02(*tuple_01))


# 关键字参数  ** 关键字参数 -> kw
# name, age 为必选参数
def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other:', kw)


person('ll', 20)
# 可传入任意关键字参数
person('pl', 24, city='BeiJing', job='FE')

extra = {
    'city': 'BeiJing',
    'job': 'Fe'
}
person('PL', '24', **extra)

# 命名关键字参数
def person_02(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass # 占位符
    if 'job' in kw:
        pass
    print('name ->', name, 'age ->', age, kw)
person_02('ll', 22, job = 'fe')

# 传入字典时
def foo(*obj):
# def foo(**obj):
    print(obj)
# foo(**{'name': 'lp'})
# foo(info={'name': 'lp'})
foo(*[1, 2, 3], *[4, 5, 6])
