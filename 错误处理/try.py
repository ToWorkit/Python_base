try:
  print('try')
  # 注意差看区别
  # r = 10 / 0
  r = 10 / 2
  print('result:', r)
except ZeroDivisionError as e:
  print('except: ', e)
finally:
  print('finally')  
print('END')
