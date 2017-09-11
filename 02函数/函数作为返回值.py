# def calc_sum(*args):
#   ax = 0
#   for n in args:
#     ax += n
#   return ax
# print(calc_sum(1, 2, 3))

# 函数作为返回值
def lazy_sum(*args):
  def sum():
    ax = 0
    for n in args:
      ax += n
    return ax
  return sum 
print(lazy_sum(1, 2, 3)())
print(lazy_sum(3, 3, 3)())
