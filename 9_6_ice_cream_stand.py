class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_server = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name},{self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is available')

    def set_numer_served(self, number):
        self.number_server = number

    def increment_number_served(self):
        self.number_server += 1


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print(self.flavors)


ice_cream_stand = IceCreamStand("DQ", 'IceCream',
                                ['Banana', 'Chocolate', 'Mango'])
ice_cream_stand.show_flavors()