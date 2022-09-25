class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name},{self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is available')


niu_rou_fen = Restaurant('Qianxi', 'Beef')
niu_rou_fen.describe_restaurant()

suan_tang_yu = Restaurant('KaiLi', 'Fish')
suan_tang_yu.describe_restaurant()

nuo_mi_fan = Restaurant('ZhenFeng', 'Rice')
nuo_mi_fan.describe_restaurant()
