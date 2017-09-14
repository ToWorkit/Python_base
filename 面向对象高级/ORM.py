# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来

# 定义一个User类来操作对应的数据库表User
class User(Model):
  # 定义类的属性到列的映射
  id = IntegerField('id')
  name = StringField('username')
  email = StringField('email')
  password = StringField('password')

# 创建一个实例
u = User(id = 12345, name = 'Test', email='test@qq.com', password="pw")
# 保存到数据库
u.save()

# Field类，负责保存数据库表的字段名和字段类型
class Field(object):
  def __init__(self, name, column_type):
    self.name = name
    self.column_type = column_type
  def __str__(self):
    return '<%s : %s>' % (self.__class__.__name__, self.name)  
# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等
class StringField(Field):
  def __init__(self, name):
    super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
  def __init__(self, name):
    super(IntegerField, self).__init__(name, 'bigint')

# ModelMetaclass
class ModelMetaclass(type):
  def __new__(cls, name, bases, attrs):
    if name == 'Model':
      return type.__new__(cls, name, bases, attrs)
    print('Found model: %s' % name)
    mappings = dict()
    for k in mappings.keys():
      attrs.pop(k)
    # 保存属性和列的映射关系  
    attrs['__mappings__'] = mappings
    # 假设表名和类名一致
    attrs['__table__'] = name
    return type.__new__(cls, name, bases, attrs)

# Model
class Model(dict, metaclass = ModelMetaclass):
  def __init__(self, **kw):
    super(Model, self).__init__(**kw)
  def __getattr(self, key):
    try:
      return self[key]
    except KeyError:
      raise AttributeError("'Model' object has no attribute '%s'" % key)
  def __setattr__(self, key, value):
    self[key] = value       
  def save(self):
    fields = []
    params = []
    args = []
    for k, v in self.__mappings__.items():
      fields.append(v.name)
      params.append('?')
      args.append(getattr(self, k, None))
    sql = 'insert into %s (%s) values (%s)' %s (self.__table__, ','.join(fields), ','.join(params))
    print('SQL: %s' % sql)
    print('ARGS: %s' % str(args))    

# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000
