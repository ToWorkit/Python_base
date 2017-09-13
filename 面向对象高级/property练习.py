class Screen(object):
  # 可操作
  @property
  def width(self):
    return self._width
  # 设置  
  @width.setter
  def width(self, value):
    # 校验
    if not isinstance(value, int):
      raise ValueError('width must interger')
    self._width = value  
  @property
  def height(self):
    return self._height
  @height.setter
  def height(self, value):
    # 校验
    if not isinstance(value, int):
      raise ValueError('height must interger')
    self._height = value  
  # 只读属性
  @property
  def resolution(self):
    return 'resolution: %d' % (self._width * self._height)
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
