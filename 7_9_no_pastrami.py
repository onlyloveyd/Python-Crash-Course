sandwich_orders = ['pastrami', 'java', 'pastrami', 'kotlin', 'pastrami', 'c++',
                   'python']

PASTRAMI = 'pastrami'
print('pastrami is out of order')
while PASTRAMI in sandwich_orders:
    sandwich_orders.remove(PASTRAMI)

print(sandwich_orders)
