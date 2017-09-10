def person(name, age, **kw):
    if 'city' in kw:
        pass  # 占位符
    if 'job' in kw:
        pass  # 占位符(表示需要做但暂时不做)
    print('name:', name, 'age:', age, 'other:', kw)


# 传入不受限制的关键字参数
person('jl', 24, city='Beijing', addr='Chaoyang', zipcode=12)
