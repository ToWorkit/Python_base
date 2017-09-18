# python 对象转 json
import json
d = dict(name = 'Bob', age = 20, score = 88)
# 返回一个str，内容为JSON
# 可以将JSON写入一个文件对象
json.dumps(d)
print(d) 
'''
要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
'''
json_str = '{"age": 20, "score": 90, "name": "Lp"}'
print(json.loads(json_str))
# JSON标准规定编码为UTF-8

# JSON进阶
import json
class Student(object):
  def __init__(self, name, age, score):
    self.name = name
    self.age = age
    self.score = score
# JSON 转换函数
def student_dict(std):
  return {
    'name': std.name,
    'age': std.age,
    'score': std.score
  }    
# 实例化
s = Student('Pl', 20, 90)

# Student的实例 s 首先被student_dict()函数转换成dict， 再序列化为JSON
# print(json.dumps(s, default = student_dict))

# 再遇到另外类的实例可以将实例变为dict
'''
  因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。

  同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
'''
print(json.dumps(s, default = lambda obj: obj.__dict__))
