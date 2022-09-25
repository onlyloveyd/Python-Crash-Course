def city_country(city, country='China'):
    return f'{city},{country}'


print(city_country('WuHan'))
print(city_country(city='XiAn'))
print(city_country('Kuala Lumpur', 'Singapore'))
