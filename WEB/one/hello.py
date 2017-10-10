# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432012393132788f71e0edad4676a3f76ac7776f3a16000
# environ：一个包含所有HTTP请求信息的dict对象；
# start_response：一个发送HTTP响应的函数。
def application(environ, start_response):
  start_response('200 OK', [('Content-type', 'text/html')])
  body = '<h1>Hello,%s</h1>' % (environ or 'web')
  # 请求方法
  # environ['REQUEST_METHOD']
  # 请求路由
  # environ['PATH_TNFO']
  return [body.encode('utf-8')]
