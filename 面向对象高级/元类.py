# type()
# type() 函数可以查看一个类型或者变量的类型

# 定义函数
def fn(self, name =  'world'):
  print('Hello, %s' % name)
# 创建 Hello class
Hello = type('Hello', (object, ), dict(hello = fn))
h = Hello()
h.hello()
# Hello 是一个class 类型是 type
print(type(Hello))
# h 是一个 实例，类型是 class Hello
print(type(h))

# metaclass
# metaclass，直译为元类，简单的解释就是：当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

# metaclass 是类的模块，所以必须从 type 类型派生
class ListMetaclass(type):
  def __new__(cls, name, bases, attrs):
    attrs['add'] = lambda self, value : self.append(value)
    return type.__new__(cls, name, bases, attrs)

# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass
class MyList(list, metaclass = ListMetaclass):
  pass

# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000

# __new__()方法接收到的参数依次是：

# 当前准备创建的类的对象；

# 类的名字；

# 类继承的父类集合；

# 类的方法集合。

# MyList 可以 调用 add() 方法
L = MyList()
L.add(2)
print(L)
# 普通的list没有add()方法
l2 = list()
# l2.add(3) # 'list' object has no attribute 'add'
