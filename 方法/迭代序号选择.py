permission_list = [
  {'caption': '添加', 'func': 'add'},
  {'caption': '删除', 'func': 'delete'},
  {'caption': '查看', 'func': 'fetch'}
]

# 添加序号，从1开始
for index, item in enumerate(permission_list, 1):
  print(index, item['caption'])

choice = '1'
choice = int(choice)
print(permission_list[choice - 1]['func'])
