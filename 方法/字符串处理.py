a = 'AAAABBBCCDAABBB'
d = list()
list(map(lambda x: (x < len(a) - 1) and (a[x] != a[x + 1]) and d.append(a[x]), range(len(a))))
d.append(a[-1])
print(d)


def unique_in_order(iterable):
    l = list()
    list(map(lambda x: (x < len(iterable) - 1) and (iterable[x] != iterable[x + 1]) and l.append(iterable[x]), range(len(iterable))))
    l.append(iterable[-1])
    return l

print(unique_in_order('AAAABBBCCDAABBBC'))
