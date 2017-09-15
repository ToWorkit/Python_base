# 内存中读写 str

# from io import StringIO
# f = StringIO()
# print(f.write('Hello'))
# print(f.write(' '))
# print(f.write('World!'))
# print(f.getvalue())


from io import StringIO
f = StringIO('Hello\nLP')
while True:
  s = f.readline()
  if s == '':
    break
  print(s.strip())  
