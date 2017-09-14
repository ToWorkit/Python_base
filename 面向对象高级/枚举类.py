from enum import Enum
# 枚举常量
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 枚举所有成员
for name, member in Month.__members__.items():
  print(name, '=>', member, ',', member.value)
# value 属性是自动赋给成员的int常量，默认从 1 开始

# 精准的控制枚举类型，可以从Enum派生出自定义类
from enum import Enum, unique
# @unique 装饰器可以检查并保证没有重复值
@unique
class Weekday(Enum):
  # Sun 的 value 被设定为 0
  Sun = 0
  Mon = 1
  Tue = 2
  Wed = 3
  Thu = 4
  Fri = 5
  Sat = 6

# 访问
day1 = Weekday.Mon
print(day1)
print(day1.value)
for name, member in Weekday.__members__.items():
  print(name, '=>', member)
