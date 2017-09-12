# 使用type()函数判断对象类型
print(type(123))
print(type(abs))
print(type('str'))
# 使用 types 模块中定义的常量
import types
def fn():
  pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x : x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
# 能用 type() 判断的基本类型也可以使用isinstance() 判断
print(isinstance('a', str))
# 还可以判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple))) # True

# dir() 获得一个对象的所有属性和方法
print(dir('str')) # 字符串的所有属性和方法
