# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432012745805707cb9f00a484d968c72dbb7cfc90b91000
# Flask web框架

# 处理3个URL
# GET /：首页，返回Home；
# GET /signin：登录页，显示登录表单；
# POST /signin：处理登录表单，显示登录结果
# 同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中
# Flask通过Python的装饰器在内部自动地把URL和函数给关联起来
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  return '<h1>Welcome Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
  return  '''
            <form action="/signin" method="post">
              <p><input name="username" /></p>
              <p><input name="password" type='password' /></p>
              <p><button type="submit">Sign In</button></p>
            </form>
          '''

@app.route('/signin', methods=['POST'])
def signin():
  # 需要从request对象读取表单内容
  if request.form['username'] == 'admin' and request.form['password'] == '123':
    return '<h2>Hello %s </h2>' % request.form['username']
    # pass
  return '<h1>用户名或密码错误</h1>'

# 文件作为脚本直接执行
# 使用 import 到其他脚本中不会被执行
if __name__ == '__main__':
  app.run()
