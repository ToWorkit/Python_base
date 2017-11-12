import time
# def now():
#   # 获取当前时间并格式化
#   print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# f = now
# f()
# print(f)
# # 可以通过__name__属性拿到函数的名字
# print(now.__name__)
# print(f.__name__)

# 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式称之为装饰器
def log(func):
  # * tuple形式，** 哈希(键值对)形式
  def wrapper(*args, **kw): 
    # call now_(): 占位
    print('call %s():' %func.__name__)
    return func(*args, **kw)
  return wrapper
# decorator (装饰器)
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now_():
  print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# 调用now_()函数，不仅会运行now_()本身，还会在运行now_()函数前打印一行日志
now_()  
