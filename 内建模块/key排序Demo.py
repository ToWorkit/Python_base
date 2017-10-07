# OrderedDict 
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict：
# 可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key

from collections import OrderedDict
class LastUpdatedOrderedDict(OrderedDict):
  def __init__(self, capacity):
    super(LastUpdatedOrderedDict, self).__init__()
    self._capacity = capacity
  def __
