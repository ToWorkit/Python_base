import copy

# 信用卡可关联账户
husband = ['Lp', 123, [99999999, 9999999]]

wife = husband.copy()
# 独立的关联账户
wife[0] = 'Pl'
wife[1] = 321
# 小三(老婆不知道) 需要独立出来，数据互不影响
xiaosan = copy.deepcopy(husband)
xiaosan[0] = 'en'
xiaosan[1] = 320
# 公用的
husband[2][1] -= 1000
# 不影响数据
xiaosan[2][0] -= 2000

print(xiaosan)
print(wife)

