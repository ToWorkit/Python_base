# continue 可以跳过当前的循环，直接开始下一次循环
num = 0
while num < 10:
    num += 1
    if num % 2 == 0: # 如果 n 是偶数，执行continue语句
        continue # continue 语句会直接继续下一轮循环，后续的print()语句不会执行
    print(num)