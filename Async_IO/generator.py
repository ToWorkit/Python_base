# 协程

# 在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。

#传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。

# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：

# 消费者
def consumer():
  r = ''
  while True:
    n = yield r
    if not n:
      return
    print('[CONSUMER] Consumer %s' % n)
    r = '200 OK'  

# 生产者
def produce(c):
  # 启动生成器
  c.send(None)
  n = 0
  while n < 5:
    n += 1
    print('[PRODUCER] Producing %s' % n)
    # 切换到consumer执行，并通过yield将结果返回
    r = c.send(n)
    print('[PRODUCER] Consumer return %s' % r)
  # 都处理完成之后结束  
  c.close()
c = consumer()
produce(c)    
