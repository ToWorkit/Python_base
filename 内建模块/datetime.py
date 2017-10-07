# 处理日期和时间
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 命令行执行
from datetime import datetime
print(datetime.now())

# str 转换为datetime
datetime.strptime('2017-10-15 20:00:00', '%Y-%m-%d %H:%M:%S')

# datetime 转换为str
now = datetime.now()
now.strftime('%a, %d %d %H:%M')

