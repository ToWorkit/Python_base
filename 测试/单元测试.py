# 单元测试 用来对一个模块，一个函数或者一个类来进行正确性检测的测试工作
class Dict(dict):
  def __int__(self, **kw):
    super().__init__(**kw)
  def __getattr__(self, key):
    try:
      return self[key]
    except KeyError:
      raise AttributeError(r"'Dict' object has no attribute '%s'" % key)    
  def __setattr__(self, key, value):
    self[key] = value

# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319170285543a4d04751f8846908770660de849f285000

# unittest
# import unittest
# from mydict import Dict
# class TestDict(unittest.TestCase):
#   def test_init(self):
#     d = Dict(a = 1, b = 'test')
#     self.assertEqual(d.a, 1)
#     self.assertEqual(d.b, 'test')
#     self.assertTrue(isinstance(d, dict))
#   def test_key(self):
#     d = Dict()
#     d['key'] = 'value'
#     self.assertEqual(d.key, 'value')
#   def test_attr(self):
#      d = Dict() 
