# 字符串大小写
username = "Eric"
print(username.lower())
print(username.upper())
print(username.title())

# 模板字符串
famous_person = "Albert Einstein"
words = "A person who never made a mistake never tried anything new."
sentence = f"{famous_person} once said, \"{words}\""
print(sentence)

# 清楚字符串空白
username = "\tyi\ndong\t"
print(username)
print(username.lstrip())
print(username.rstrip())
print(username.strip())

# 小学生四则运算
print(5 + 3)
print(11 - 3)
print(2 * 4)
print(int(16 / 2))

# 列表访问与组合
sites = ['XiAn', 'BeiJing', 'NanJing', 'QingHai', 'GanShu']
print(sites[1])
print(sites[-2])
print(len(sites))
sites[1] = "GuiYang"

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

# sort
sites.sort()
print(sites)

# 列表操作
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

# 遍历列表
pizzas = ['Seafood', 'Sausage', 'Cheese']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print('I really love pizza!')

# 区间与步长
odds = [value for value in range(1, 21, 2)]
for odd in odds:
    print(odd ** 3)

# 最大值、最小值与求和
million = [value for value in range(1, 1000_000 + 1)]
print(f"min = {min(million)}")
print(f"max = {max(million)}")
print(f"sum = {sum(million)}")

# 列表解析
times = [value ** 3 for value in range(1, 11)]
for time in times:
    print(time)

# 列表切片
sites = ['XiAn', 'BeiJing', 'NanJing', 'QingHai', 'GanShu']
print(f'The first three items in the list are:{sites[:3]}')
print(f'Three items from the middle of the list are:{sites[1:4]}')
print(f'The last three items in the list are:{sites[-3:]}')

# 列表副本
pizzas = ['Seafood', 'Sausage', 'Cheese']
friend_pizzas = pizzas[:]

# 元组（ 列表用[],元组用() ）
foods = ('Twist', 'Noodles', 'Ice Cream', 'Steamed Meat Dumpling',
         'Instant Boiled Sliced Mutton')
for food in foods:
    print(food)

# 判断语句
hello = "Hello"
world = "World"
print(hello == 'Hello')
print(hello == world)

print(hello == 'hello')
print(hello.lower() == 'hello')

score = 60
print(score < 60)
print(score == 60)
print(score > 60)

print(hello.lower() == 'hello' and score == 60)
print(hello == 'hello' or score < 60)

pizzas = ['Seafood', 'Sausage', 'Cheese']
print('seafood' in pizzas)
print('Seafood' in pizzas)

# if语句
for number in range(1, 10):
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    else:
        print(f'{number}th')

# 字典
term = {
    'Function': '函数',
    'Variance': '变量',
    'Loop': '循环',
    'Network': '网络',
    'Device': '设备',
    'Comment': '注释',
    'Keyword': '关键字',
    'Primitive': '原语',
    'Set': '集合',
    'List': '列表',
}
print(f"Function: {term['Function']}")
print(f"Variance: {term['Variance']}")
print(f"Loop: {term['Loop']}")
print(f"Network: {term['Network']}")
print(f"Device: {term['Device']}")
for key, value in term.items():
    print(f'{key}:{value}')

# 字典嵌套
cities = {
    'XiAn': {
        'country': 'China',
        'population': 100000,
        'fact': 'Beautiful'
    },
    'NewYork': {
        'country': 'American',
        'population': 12,
        'fact': 'Modern'
    },
    'Kuala Lumpur': {
        'country': 'Singapore',
        'population': 50000,
        'fact': 'Fashion'
    },
}

for key, value in cities.items():
    print(f'{key}:{value}')

# 用户输入与while循环
prompt = 'If you could visit one place in the world, where would you go?\n'
active = True
QUIT = 'quit'
results = []
while active:
    place = input(prompt)
    if place == QUIT:
        break
    else:
        results.append(place)

print(results)


# 函数形参、实参，关键字，默认参数
def make_shirt(size='大号', title='I love Python'):
    print(f'Size: {size}, Title: {title}')


make_shirt()
make_shirt('中号')
make_shirt("小号", "Python")
make_shirt(size='中号', title="Kotlin")


# 函数返回值
def make_album(name, singer, number_of_songs=None):
    return {
        'name': name,
        'singer': singer,
        'number_of_songs': number_of_songs
    }


print(make_album('name1', 'singer1'))
print(make_album('name2', 'singer2'))
print(make_album('name3', 'singer3', 9))


# 任意数量的位置实参
def make_sandwich(*toppings):
    """打印顾客点的所有配料。"""
    print(f'Sandwich: {toppings}')


make_sandwich('pepperoni')
make_sandwich('mushrooms', 'green peppers', 'extra cheese')


# 任意数量的关键字实参
def make_car(maker, category, **car_info):
    car_info['maker'] = maker
    car_info['category'] = category
    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)


# 类继承
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

    def get_range(self):
        print(self.battery_size)


class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)
        self.battery = Battery()


electric_car = ElectricCar('tesla', 'model s', 2019)
electric_car.battery.get_range()
electric_car.battery.upgrade_battery()
electric_car.battery.get_range()

# 导入包
# https://pymotw.com/3/
from random import randint, randrange, randbytes, random, getrandbits

print(randint(1, 2))
print(randrange(1, 10000, 3))
print(randbytes(10))
print(random())
print(getrandbits(5))

# 读取文件
file_path = 'learning_python.txt'
with open(file_path) as file_object:
    content = file_object.read()
print(content)

with open(file_path) as file_object:
    for line in file_object:
        print(line)

with open(file_path) as file_object:
    lines = file_object.readlines()
print(lines)

# 写入文件
name = input('Pls input you name: ')
with open(file_path, 'w') as file_object:
    file_object.write(name)

# 文件内容追加
reason = input('Why do you like programming: ')
with open(file_path, 'a') as file_object:
    file_object.write(reason + '\n')

# 异常
one = input('Pls input a number: ')
two = input('Pls input another number: ')

try:
    number_one = int(one)
    number_two = int(two)
except ValueError:
    print('Pls input number')
else:
    print(f'{number_one}+{number_two} = {number_one + number_two}')

# 文件异常
cats_file = 'cats.txt'
dogs_file = 'dogs.txt'

try:
    with open(cats_file) as cats_objects:
        print(cats_objects.read().rstrip())
    with open(dogs_file) as dogs_objects:
        print(dogs_objects.read().rstrip())
except FileNotFoundError:
    pass
else:
    print("Read Successfully")

# json读写
import json

def get_stored_username():
    """如果存储了用户名，就获取它。"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名。"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
    return username


def greet_user():
    """问候用户，并指出其名字。"""
    username = get_stored_username()
    if username:
        is_correct = input(f'Is {username} right?(yes/no)')
        if is_correct == 'yes':
            print(f"Welcome back, {username}!")
        else:
            get_new_username()
    else:
        get_new_username()


greet_user()

# 测试代码
import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.default_salary = 100000
        self.employee = Employee("Yi", "Dong", self.default_salary)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, self.default_salary + 5000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, self.default_salary + 10000)


if __name__ == "__main__":
    unittest.main()
