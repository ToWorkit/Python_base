# f = open('test.txt', 'w', encoding='utf8')
# append 追加模式
f = open('test.txt', 'a', encoding='utf8')
# 截断， 默然参数 清空, 光标定位到开始处， 有参数时则截取参数个并定位到参数处
f.truncate(1)
# print(tr)
f.write('Hello World')
f.truncate(2)
f.close()
