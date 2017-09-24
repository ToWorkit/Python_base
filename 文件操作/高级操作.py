# r+ 对写模式
f = open('test.txt', 'a+', encoding='utf8')
# for line in f:
#   print(line)
'''
import sys
for i, v in enumerate(f):
  # sys.stdout.write(v + '--->' + str(i))
  print(v, i)
'''
f.seek(0)
num = 0
for i in f:
  num += 1
  if num == 3:
    print(i)
    # i = ''.join([i.strip(), '<----'])
    
    # f.write('<------')

f.close()

