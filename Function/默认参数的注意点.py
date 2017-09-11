def add_end(arr = []):
    arr.append('END')
    return arr
# 正确
print(add_end([1, 2, 3]))
# 但是不传递其他参数，只使用默认参数时就会出现累加的效果(BUG)
print(add_end())
print(add_end())
# 默认参数必须指向不可变的对象
# 修改
def add_n(arr = None):
    if arr is None:
        arr = []
    arr.append('And')
    return arr
print(add_n())
print(add_n())
print(add_n([2, 1, 0]))