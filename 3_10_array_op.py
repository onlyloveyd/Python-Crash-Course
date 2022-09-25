sites = ['XiAn', 'BeiJing', 'NanJing', 'QingHai', 'GanShu']
sites.insert(0, "GuiYang")
print(sites)

print(sites.pop())

del sites[0]
sites.remove('XiAn')

print(sites)

print(len(sites))

sites[-1] = "WuHan"
print(sites)
