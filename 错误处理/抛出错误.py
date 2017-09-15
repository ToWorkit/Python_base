# class类型的，捕获一个错误就是捕获到该class的一个实例
# 使用 raise 抛出错误
class FooError(ValueError):
  pass
def foo(s):
  n = int(s)
  if n == 0:
    # 定义错误
    raise FooError('invalid value: %s' % s)
  return 10 / n
foo('0')
