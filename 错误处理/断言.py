# 用到print()来辅助查看的地方，使用断言assert来代替
def foo(s):
  n = int(s)
  assert n != 0, 'n is zero!'
  return 10 / n
def main():
  foo('0')

main()
