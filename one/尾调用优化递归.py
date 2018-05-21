def fact(n, p = 1):
  if n <= 1:
    return p
  # n * p 在函数调用之前就计算了，不会影响函数调用
  return fact(n - 1, n * p)

# print(fact(5))   



# def unique_in_order(iterable):
    




# print(unique_in_order('AAAABBBCCDAABBB'))

a = 'AAAABBBCCDAABBB'
b = a[:]
c = list()
print(type(b))
for i in range(len(a)):
  if((i < len(a) - 1) and (a[i] != a[i + 1])):
    c.append(a[i])
c.append(a[-1])
print(c)
print(a[-1])




v = set()
v.update(a)
print(v) # {'B', 'C', 'D', 'A'}



