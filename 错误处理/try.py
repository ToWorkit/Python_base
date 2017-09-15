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
print('------------------')
# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”

def foo(s):
  return 10 / int(s)
def bar(s):
  print(foo(s) * 2)
def main():
  try:
    bar('2')
  except Exception as e:
    print('Error:', e)
  finally:
    print('Finally')        

main()
