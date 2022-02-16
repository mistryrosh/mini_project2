import csv
import products
import couriers
from pprint import pp
from telnetlib import STATUS
from typing import OrderedDict


def menu():
  main_menu = '''
  [0] To return to main menu
  [1] To view order
  [2] To add to order
  [3] To update ordaer status
  [4] To update an existing order
  [5] To Delete an order  "\n" '''
  
  print(main_menu)

def add_to_order(product, customer_name, customer_address, customer_phone, courier):
      product = products.get_product_name(product)
      courier = couriers.get_courier_name(courier)
  
      order_info = {
      "product": product,
      "customer_name": customer_name,
      "customer_addresss": customer_address,
      "customer_phone": customer_phone,
      "courier": courier,
      "order_status": "preparing"
      }
      # pp(order_info)

      fieldnames = ['product', 'customer_name', 'customer_addresss', 'customer_phone', 'courier', 'order_status']
      try:
        with open('database/orders.csv', 'a', newline="") as file:
          writer = csv.DictWriter(file, fieldnames=fieldnames)
          # writer.writeheader()
          writer.writerow(order_info)
      except Exception as error1:
        print("failed to execute order", error1)
      else:
        print('your order is being processed')  
    
# add_to_order("soda", "peter", "25 street street kingston", "097645", "kenny", "out for delievery")

def view_order():
  item_num = 1
  with open('database/orders.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:    
        print(f"{item_num}."," ".join(row)) # join all items of a list into a sentence on the same row e.g add to orders
        item_num += 1

# view_order()


def update_existing_order(product, customer_name, customer_address, customer_phone, courier, order_index):
    item_num = 1
    orders = []
    product = products.get_product_name(product)
    courier = couriers.get_courier_name(courier)
    with open('database/orders.csv', 'r') as file:
      reader = csv.reader(file)
      # next(reader)
      for row in reader:    
          if item_num == order_index:
            row[0] = product # putting all the items i.e product, customer name etc on the same row
            row[1] = customer_name
            row[2] = customer_address
            row[3] = customer_phone
            row[4] = courier 
          orders.append(row)
          item_num += 1

    with open('database/orders.csv', 'w', newline="") as f:
      write = csv.writer(f) 
      write.writerows(orders)

# update_existing_order("water", "tom", "65 street", "786546" , "uber eats", 4)

def update_order_status(order_status, order_id):
    item_num = 1
    orders = []
    with open('database/orders.csv', 'r') as file:
      reader = csv.reader(file)
      for row in reader:    
          if item_num == order_id:
            row[5] = order_status
          orders.append(row)
          item_num += 1

    with open('database/orders.csv', 'w', newline="") as f:
      write = csv.writer(f) 
      write.writerows(orders)

# update_order_status("on its way", 1)

def delete_order_item(order_id):
    orders = []
    with open('database/orders.csv', 'r') as file:
      reader = csv.reader(file)
      for row in reader:                                                    
        orders.append(row)                  
      del orders[order_id-1]
      # pp(orders)
 
    with open('database/orders.csv', 'w', newline="") as f:
      write = csv.writer(f) 
      write.writerows(orders)

# delete_order_item(5)
