i = 7
while i > 0:
  flag = i
  while flag > 0:
    # 当前一行并列间隔符 end = '&'(符号可以自定义)
    print('*', end = '')
    flag -= 1
  print()  
  i -= 1  
