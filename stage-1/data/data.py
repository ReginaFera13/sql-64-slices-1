import csv
import re

orders = []
def get_orders(file):
    with open(file, mode='r', newline='') as csvfile:
        order_data_reader = csv.DictReader(csvfile)
        for row in order_data_reader:
            order_num = int(row['order_id'])
            toppings_slash = row['toppings']
            
            order = {
                'order_id': order_num,
                'toppings': toppings_slash
            }
            
            orders.append(order)

get_orders('/home/reginafera13/codeplatoon/sql-64-slices-1/stage-1/data/orders.csv')

# print(orders)

formatted_orders = []

def format_orders(orders):
    for order in orders:
        order_id = order['order_id']
        toppings = order['toppings'].split('/')
        for topping in toppings:
            # print(f'order_id: {order_id} | topping: {topping}')
            formatted_order = {
                'order_id': order_id,
                'topping': int(topping)
            }
            formatted_orders.append(formatted_order)

format_orders(orders)

print(formatted_orders)