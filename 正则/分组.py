import re
# 定义两个组
# ^(\d{3})-(\d{3,8})$
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
