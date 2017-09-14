import os
import requests
# 打印当前工作路径
print(os.getcwd())
# 抓取百度
r = requests.get('https://www.tmall.com')
print(r.url)
# 网页编码
print(r.encoding)
# 获取网页html
print(r.text)
