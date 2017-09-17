# 字符串占位符 %s   string
# 整数占位符   %d   digit
# 浮点数占位符 %f   float
name = input('Name: ')
age = input('Age: ')
job = input('Job: ')
salary = input('Salary: ')
# 判断长得像不像数字
if salary.isdigit():
    salary = int(salary)
else:
    # print('mut input digit')
    exit('mut input digit') # 不满足条件则停止继续执行程序

# 占位符同样要求格式
msg = '''
---------info of %s ---------
Name: %s
Age: %d
Job: %s
Salary: %s
You will be retired in %s years # 多久退休
---------end ----------------
''' % (name, name, int(age), job, salary, 9999999999 - int(age))
print(msg)