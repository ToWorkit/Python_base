#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "LC"

import asyncio, logging
import aiomysql

def log(sql, args=()):
  logging.info('SQL: %s' % sql)

'''
  创建数据库连接池
   loop 事件循环处理程序
   kw   数据库配置参数集合
'''
async def create_pool(loop, **kw):
  logging.info('Create SQL Connection Pool')
  # 创建全局变量
  global __pool
  # 初始化连接池参数
  __pool = await aiomysql.create_pool(
    host = kw.get('host', 'localhost'),
    port = kw.get('port', 3306),
    user = kw['user'],
    password = kw['password'],
    db = kw['db'],
    charset = kw.get('charset', 'utf-8'),
    autocommit = kw.get('autocommit', True),
    maxsize = kw.get('maxsize', 10),
    minsize = kw.get('minsize', 1),
    loop = loop
    )

'''
  数据库查询函数
    sql  SQL语句
    args SQL语句中的参数
    size 需要查询的数量
  return 查询结果  
'''
async def select(sql, args, size=None):
  log(sql, args)
  global __pool
  async with __pool.get() as conn:
    # 创建一个结果为字典的游标
    async with conn.cursor(aiomysql.DictCursor) as cur:
      # 执行sql语句，将SQL语句中的 '?' 替换位 '%s'
      await cur.execute(sql.replace('?', '%s'), args or ())
      # 如果指定了数量就返回指定数量的记录，没有就返回所有记录
      if size:
        rs = await cur.fetchmany(size)
      else:
        rs = await cur.fetchall()
    logging.info('返回的记录数: %s' % len(rs))
    return rs

'''
  Insert, Update, Delete 操作的公共执行函数
    sql  SQL语句
    args SQL参数
    autocommit 自动提交事务
''' 
async def execute(sql, args, autocommit=True):           
  log(sql)
  async with __pool.get() as conn:
    if not autocommit:
      await conn.begin()
    try:
      # 创建游标
      async with conn.cursor(aiomysql.DictCursor) as cur:
        # 执行SQL语句
        await cur.execute(sql.replace('?', '%s'), args or ())
        # 获取操作的记录数
        affected = cur.rowcount
      if not autocommit:
        await conn.commit()
    # 异常    
    except BaseException as e:
      if not autocommit:
        # 回滚
        await conn.rollback()
      raise
    return affected  

class ModelMetaclass(type):
  '''
    创建模型与表映射的基类
      name  类名
      bases 父类
      attrs 类的属性列表
    return 模型元类
  '''
  def __new__(cls, name, bases, attrs):
    # 排除Model类本身
    if name == 'Model':
      return type.__new__(cls, name, bases, attrs)
    # 获取表名，如果没有表名则将类名作为表名
    tableName = attrs.get('__table__', None) or name
    logging.info('模型：%s (表名: %s)' % (name, tableName))
    # 获取所有的类属性和主键名  
    
    # 储存属性名和字段信息的映射关系
    mappings = dict()
    # 储存所有非主键的属性
    fields = []
    # 储存主键属性
    primaryKey = None

    # 遍历attrs(类的所有属性)，k为属性名，v为该属性对应的字段信息
    for k, v in attrs.items():
      # 如果v是自己定义的字段类型
      if isinstance(v, Field):
        logging.info('映射关系: %s ==> %s' % (k, v))
        # ↑
        # 储存映射关系 
        mappings[k] = v
        # 如果该属性是主键
        if v.primary_key: 
          # 如果primaryKey已经保存了主键，说明主键重复
          if primaryKey:
            # 抛出错误
            raise RuntimeError('主键重复: 在 %s 中的 %s' % (name, k))
          primaryKey = k 
        # 不是则储存到fields中  
        else:  
          fields.append(k)

    # 如果遍历完成没有找到主键则主键没有定义
    if not primaryKey:
      raise StandardError('主键未定义')
    # 清空attrs
    for k in mappings.keys():
      attrs.pop(k)
    # 将fields中属性名以`属性名`的方式装饰起来
    escaped_fields = list(map(lambda f : '`%s`' % f, fields))
    # 重新设置 attrs
    # 保存属性和字段信息的映射关系
    attrs['__mappings__'] = mappings
    # 保存表名
    attrs['__table__'] = tableName
    # 主键属性名
    attrs['__primary_key__'] = primaryKey
    # 除主键外的属性名
    attrs['__fields__'] = fields

    # 构造默认的SELECT，INSERT，UPDATE，DELETE语句
    attrs['__select__'] = 'select `%s` , %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
    attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
    attrs['__update__'] = 'update `%s` set %s where `%s` =?' % (tableName, ', '.join(map(lambda f : '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
    attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
    return type.__new__(cls, name, bases, attrs)

'''
  用来计算需要拼接多少个占位符
'''  
def create_args_string(num):
  L = []
  for n in range(num):
    L.append('?')
  return ', '.join(L)

# 属性(非主键)

class Field(object):
  def __init__(self, name, column_type, primary_key, default):
    self.name = name
    self.column_type = column_type
    self.primary_key = primary_key
    self.default = default
  def __str__(self):
    return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)

class StringField(Field):
  def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
    super().__init__(name, ddl, primary_key, default)

class BooleanField(Field):
  def __init__(self, name=None, default=False):
    super().__init__(name, 'boolean', False, default)

class IntegerField(Field):
  def __init__(self, name=None, primary_key=False, default=0):
    super().__init__(name, 'bigint', primary_key, default)

class FloatField(Field):
  def __init__(self, name=None, primary_key=False, default=0.0):
    super().__init__(name, 'real', primary_key, default)

class TextField(Field):
  def __init__(self, name=None, default=None):
    super().__init__(name, 'text', False, default)

class Model(dict, metaclass=ModelMetaclass):
  def __init__(self, **kw):
    super(Model, self).__init__(**kw)
  def __getattr__(self, key):
    try:
      return self[key]
    except KeyError:
      raise AttributeError(r"'Model' object has no attribute '%s'" % key)
  def __setattr__(self, key, value):
    self[key] = value
  def getValue(self, key):
    return getattr(self, key, None)
  def getValueOrDefault(self, key):
    value = getattr(self, key, None)
    # 如果没有找到value
    if value is None:    
      # 从mappings映射集合中找
      field = self.__mappings__[key]
      # 可调用
      value = field.default() if callable(field.default) else field.default
      logging.debug('使用默认值 %s:%s' % (key, str(value)))
      setattr(self, key, value)
    return value  

  '''
    通过where查找多条记录对象
      where  where查询条件
      args   SQL参数
      kw     查询条件列表
    return 多条记录集合  
  '''
  @classmethod
  async def findAll(cls, where=None, args=None, **kw):
    sql = [cls.__select__]
    # 如果where查询条件存在
    if where:
      # 添加where关键字
      sql.append('where')
      # 拼接where查询条件
      sql.append(where)
    if args is None:
      args = []
    # 获取kw里面的orderBy查询条件  
    orderBy = kw.get('orderBy', None)    
    # 如果存在orderBy
    if orderBy:
      # 拼接orderBy字符串
      sql.append('orderBy')
      # 拼接orderBy查询条件
      sql.append(orderBy)
    # 获取limit查询条件
    limit = kw.get('limit', None)
    if limit is not None:
      sql.append('limit')
      # 如果limit是int类型
      if isinstance(limit, int):
        # SQL拼接一个占位符
        sql.append('?')  
        # 将limit添加进参数列表
        # 添加参数列表之后再进行整合可以防止SQL注入
        args.append(limit)
      # 如果limit是一个tuple类型并且长度是2
      elif isinstance(limit, tuple) and len(limit) == 2:
        # sql语句拼接两个占位符
        sql.append('?,?')
        # 将limit添加进参数列表
        # extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
        args.extend(limit)
      else:
        raise ValueError('limit参数无效: %s' % str(limit))
    # 将args参数列表注入sql语句之后，传递select函数进行查询并返回查询结果
    rs = await select(''.join(sql), args)
    return [cls(**r) for r in rs]
  
  '''
    查询某个字段的数量
      selectField   要查询的字段
      where         where查询条件
      args          参数列表
    return 数量
  '''
  @classmethod
  async def findNumber(cls, selectField, where=None, args=None):   
    sql = ['select count(%s) _num_ from `%s`' % (selectField, cls.__table__)]
    if where:
      sql.append('where')
      sql.append(where)
    rs = await select(''.join(sql), args, 1)
    return rs[0]['_num_']

  '''
    通过id查询
      pk  id
    return 一条记录  
  '''  
  @classmethod
  async def findById(cls, pk):    
    rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
    if len(rs) == 0:
      return None
    return cls(**rs[0])
  
  '''
    通过指定字段查询
      f   要查询的字段
      cl  查询字段所对应的值
    return 一条记录  
  '''
  @classmethod
  async def findByColumn(cls, f, cl):
    fi = None
    # 遍历属性列表查看是否存在
    for field in cls.__fields__:
      # 有则赋值给fi然后退出循环
      if f == field:
        fi = field
        break
    if fi is None:
      raise AttributeError('在%s中没有找到该字段' % cls.__table__)
    rs = await select('%s where `%s`=?' % (cls.__select__, fi), [cl], 1)
    if len(rs) == 0:
      return None
    return cls(**rs[0])     

  async def save(self):
    # 将__fields__保存的除主键外的所有属性一次性传递到getValueOrDefault函数中获取值
    args = list(map(self.getValueOrDefault, self.__fields__))
    # 获取主键值
    args.append(self.getValueOrDefault(self.__primary_key__))
    # 执行insertsql语句
    rows = await execute(self.__insert__, args)
    if rows != 1:
      logging.warning('插入记录失败,第 %s 行受影响' % rows)

  async def update(self):
    args = list(map(self.getValue, self.__fields__))
    args.append(self.getValue(self.__primary_key__))
    rows = await execute(self.__update__, args)
    if rows != 1:
      logging.warning('更新记录失败，第 %s 行受影响' % rows)

  async def delete(self):
    args = [self.getValue(self.__primary_key__)]
    rows = await execute(self.__delete__, args)
    if rows != 1:
      logging.warning('删除记录失败，第 %s 行受影响' % rows)        
