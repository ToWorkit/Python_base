# -*- coding: utf-8 -*-
import functools
import time
# 使用默认参数
def log(text = 'call'):
  def decorator(func):
    # 防止__name__被篡改
    @functools.wraps(func)
    def wrapper(*args, **kw):
      try:
        print('%s %s %s():' %('begin', text, func.__name__))
        return func(*args, **kw)
      # 完成后
      finally:
        print('%s %s %s():' %('end', text, func.__name__))  
    return wrapper
  return decorator

@log()
def now_01():        
  print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

@log('第一个是默认参数的，这个是传入参数的')
def now_02():
  print(time.strftime('%Y/%m/%d %H-%M-%S', time.localtime()))

now_01()
now_02()  
