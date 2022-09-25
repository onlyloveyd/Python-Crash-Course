def make_car(maker, category, **car_info):
    car_info['maker'] = maker
    car_info['category'] = category
    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
