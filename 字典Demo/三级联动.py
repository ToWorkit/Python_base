menu = {
  "北京": {
    "朝阳": {
      "奥森": {},
      "天安门": {}
    },
    "海淀": {
      '五道口': {},
      '北航': {}
    }
  },
  "西安": {
    "钟楼": {},
    "鼓楼": {},
    "小寨": {}
  }
}
# 当前字典
current_layer = menu
# 父级字典
parent_layers = []
while True:
  for key in current_layer:
    print(key)
  # 用户输入选择
  choice = input('请选择: ').strip()
  # 如果没有选择就继续循环接着选
  if len(choice) == 0:continue  
  # 有所选择的
  if choice in current_layer:
    # 当前级就变成了父级
    parent_layers.append(current_layer)
    # 子级
    current_layer = current_layer[choice]
  elif choice == 'b': # 退出
    if parent_layers:
      # 返回上一级
      current_layer = parent_layers.pop()
  else:
    print('查无此项')
