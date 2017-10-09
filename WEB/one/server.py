# wsgiref
from wsgiref.simple_server import make_server
# 导入自己写的application函数
from hello import application

# 创建服务器,IP地址为空,端口为8000，处理函数是application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000')
# 开始监听HTTP请求
httpd.serve_forever()
