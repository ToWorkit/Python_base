# 集合

# tuple 不变集合

# namedtuple 来创建一个表示坐标的集合
# namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
# 验证创建的Point对象是tuple的一种子类
print(isinstance(p, Point))
print(isinstance(p, tuple))

# 坐标和半径表示一个圆
# namedtuple('名称', [属性list])
Circle = namedtuple('Circle', ['x', 'y', 'r'])


# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)


# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
from collections import defaultdict
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
dd = defaultdict(lambda: 'DEFAULT')
dd['a'] = 'abc'
print(dd['a'])
print(dd['v'])


# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
