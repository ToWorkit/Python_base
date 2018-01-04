# -*- coding: utf-8 -*-
import re
def _replace(m):
  target = int(m.group(2)) + 12
  concat = m.group(1) + str(target) + m.group(3)
  return concat
# 尽量使用 with 语句操作文件
with open('old.txt', 'r', encoding = 'utf-8') as r, open('new.txt', 'w') as w:
  data = r.read()
  # print(data)
  result = re.sub(r'(第)(\d+)(章)', _replace, data)
  w.write(result)
