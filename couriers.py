import csv
from pprint import pp


def menu():
    
    Main_Menu = '''
    [0] To exit app
    [1] To view couriers list
    [2] To add new couriers
    [3] To update/replace courier 
    [4] To Delet/Remove courier "\n" '''

    print(Main_Menu)


# add item - working but not for coffee - also first item not showing on line 1 
def add_courier(courier, phone_num):
    new_courier = [courier, phone_num]
    try:
          with open('database/couriers.csv', 'a', newline='') as file:
            write = csv.writer(file) 
            write.writerow(new_courier)
    except Exception as error1:
        print("failed to execute drink", error1)

# add_courier("kangeroo", "124478")

# view menu - working
def view_courier():
    try:
        with open('database/couriers.csv', 'r') as file:
            reader = csv.DictReader(file)
            item_num = 1
            for courier in reader:
                print(f"{item_num}.", courier.get('courier'), courier.get('phone_num'))
                item_num += 1
    except Exception as error1:
        print("failed to execute drink", error1)

# view_courier()

def update_courier(name, phone_num, courier_index):
    item_num = 1
    courier = []
    with open('database/couriers.csv', 'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
          if item_num == courier_index:
              row.update({'courier': name, 'phone_num': phone_num})
        #     row[0] = name # putting all the items i.e product, customer name etc on the same row
        #     row[1] = price
          courier.append(row)
          item_num += 1   
    #   pp(courier)

    fieldnames = ['courier', 'phone_num']
    with open('database/couriers.csv', 'w', newline="") as file:
      write = csv.DictWriter(file, fieldnames=fieldnames)
      write.writeheader()
      write.writerows(courier)

# update_courier('deliveroo', "134597", 1)

def delete_courier(courier_index):
    item_num = 1
    couriers = []
    with open('database/couriers.csv', 'r') as file:
      reader = csv.DictReader(file)
      for row in reader: 
          couriers.append(row)
          item_num += 1 
      del couriers[courier_index-1] 
    #   pp(couriers)

    heading = ['courier', 'phone_num']
    with open('database/couriers.csv', 'w', newline="") as file:
      write = csv.DictWriter(file, fieldnames=heading)
      write.writeheader()
      write.writerows(couriers)

# delete_courier(5)

def get_courier_name(courier_index): #puts in order.py product = products.get_product_name(product)
    courier_name = " "
    try:
        with open("database/couriers.csv", "r") as file:
            reader = csv.DictReader(file)
            item_num = 1
            for courier in reader:
                if item_num == courier_index:
                # print(product)
                 courier_name = courier.get('courier')
                item_num += 1
    except Exception as error1:
        print("failed to execute drink", error1)
    return courier_name

# print(get_courier_name(3))