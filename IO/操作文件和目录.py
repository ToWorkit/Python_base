import os
# 查看系统名称
print(os.name)
# 查看环境变量
# print(os.environ)
# 获取某个环境变量
print(os.environ.get('PATH'))
print('--------------------')
# 操作文件和目录
# 当前 dirname
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
print(os.path.join(os.path.abspath('.'), 'testDir'))
testdir = os.path.join(os.path.abspath('.'), 'testDir')
# 然后再创建一个目录
# os.mkdir(testdir)
# 删除一个目录
# os.rmdir(testdir)

'''
  合并路径时要使用 os.path.join() 可以处理不同路径下的操作系统路径分隔符
  拆分路径时要使用 os.path.split() 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
  合并，拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
'''
print(os.path.split('/Users/hedy/Desktop/Python/IO/test.txt'))

# 直接获取到文件的扩展名
print(os.path.splitext('/Users/hedy/Desktop/Python/IO/test.txt'))

print('----------------------')

'''
  复制文件的函数在os模块中不存在，因为复制文件并非由操作系统提供的系统调用
  可以使用shutil模块提供的copyfile()实现，可以当做是os模块的补充
'''

# 对文件重命名 同一目录下
# os.rename('test.txt', 'test.py')

# 删除文件
# os.remove('test.py')

# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出所有的 .py 文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
