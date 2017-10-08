import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn', 80))
# 连接后发送请求，要求返回首页的内容
# b 字节
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接受返回的数据
buffer = []
while True:
  # 限制每次最多接受1k字节
  d = s.recv(1024)
  if d:
    buffer.append(d)
  else:
    break
data = b''.join(buffer)    

# 关闭连接
# 一次完成的网络通信
# 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 将接收的数据写入文件
with open('sina.html', 'wb') as f:
  f.write(html)
