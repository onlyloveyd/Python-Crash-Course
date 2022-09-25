sites = ['XiAn', 'BeiJing', 'NanJing', 'QingHai', 'GanShu']
print(sites)

# 使用sorted()按字母顺序打印这个列表，同时不要修改它。
print(sorted(sites))
# 再次打印该列表，核实排列顺序未变。
print(sites)

# 使用sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它。
print(sorted(sites, reverse=True))
# 再次打印该列表，核实排列顺序未变
print(sites)

# reverse
sites.reverse()
print(sites)

sites.reverse()
print(sites)

sites.sort()
print(sites)

sites.reverse()
print(sites)
