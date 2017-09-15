# logging 模块记录错误信息
import logging
def foo(s):
  return 10 / int(s)
def bar(s):
  return foo(s) * 2
def main():
  try:
    bar('0')
  except Exception as e:
    logging.exception(e)
main()
# 出错后不会中断程序
# 可以进行配置将logging的错误记录放到日志文件里
print('END')
print('------------------')
