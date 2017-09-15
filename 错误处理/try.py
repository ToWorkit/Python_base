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
print('-----------------------------')
# 多个except捕获不同类型的错误
try:
  print('try')
  r = 10 / int('5')
  print('result:', r)
except ValueError as e:
  print('ValueError:', e)
# 运算错误  
except ZeroDivisionError as e:
  print('ZeroDivisionError:', e)
else:
  print('No Error')  
finally:
  print('finally')
print('END')        
