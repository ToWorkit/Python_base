# break 语句可以提前退出循环
num = 1
while num <= 100:
    if num > 10:
        break # 当 n = 11 时， 满足条件后执行break退出循环
    print(num)
    num += 1
print('END')