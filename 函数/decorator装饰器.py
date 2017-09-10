import time
def log(text):
  def decorator(func):
    def wrapper(*args, **kw):
      print('%s %s():' % (text, func.__name__))
      return func(*args, **kw)
    return wrapper
  return decorator
@log('仔细看')
def now():
  print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
now()
# 因为返回值是 wrapper函数， 所以__name__ 会是wrapper
print(now.__name__)

# 使用functools.wraps将__name__还原
import functools
def log_(text):
  def decorator(func):
    # 指定 __name__ 为函数本身
    @functools.wraps(func)
    def wrapper(*args, **kw):
      print('%s %s():' %(text, func.__name__))
      return func(*args, **kw)
    return wrapper
  return decorator
@log_('指定后的')
def now_():
  print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

now_()
print(now_.__name__)
