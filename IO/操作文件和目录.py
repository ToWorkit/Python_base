import os
# 查看系统名称
print(os.name)
# 查看环境变量
# print(os.environ)
# 获取某个环境变量
print(os.environ.get('PATH'))
# 操作文件和目录
# 当前 dirname
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
