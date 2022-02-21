import csv
from pprint import pp


def menu():

    main_menu = '''
    [0] To return to Main Menu
    [1] To view Menu
    [2] To add new product
    [3] To update/replace product 
    [4] To Delet/Remove product "\n" '''

    print(main_menu)


# add item - working but not for coffee - also first item not showing on line 1 
def add_item(name, price):
    new_item = [name, price]
    try:
          with open('database/products.csv', 'a', newline='') as file:
            write = csv.writer(file) 
            write.writerow(new_item)
    except Exception as error1:
        print("failed to execute drink", error1)

# add_item("coke", 1.00)

# view menu - working
def products_menu():
    try:
        with open("database/products.csv", "r") as file:
            reader = csv.DictReader(file)
            item_num = 1
            for product in reader:
                # print(product)
                print(f"{item_num}.", product.get('name'), f"£{product.get('price')}")
                item_num += 1
    except Exception as error1:
        print("failed to execute drink", error1)

# products_menu()

def update_item(name, price, product_index):
    item_num = 1
    products = []
    with open('database/products.csv', 'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
          if item_num == product_index:
              row.update({'name': name,'price': price})
        #     row[0] = name # putting all the items i.e product, customer name etc on the same row
        #     row[1] = price
          products.append(row)
          item_num += 1   
    #   pp(products)

    fieldnames = ['name', 'price']
    with open('database/products.csv', 'w', newline="") as file:
      write = csv.DictWriter(file, fieldnames=fieldnames)
      write.writeheader()
      write.writerows(products)

# update_item('tropical juice', 4.50, 3)

def delete_item(product_index):
    item_num = 1
    products = []
    with open('database/products.csv', 'r') as file:
      reader = csv.DictReader(file)
      for row in reader: 
          products.append(row)
          item_num += 1 
      del products[product_index-1] 
    #   pp(products)

    heading = ['name', 'price']
    with open('database/products.csv', 'w', newline="") as file:
      write = csv.DictWriter(file, fieldnames=heading)
      write.writeheader()
      write.writerows(products)

# delete_item(3)

def get_product_name(product_index): #puts in order.py product = products.get_product_name(product)
    product_name = " "
    try:
        with open("database/products.csv", "r") as file:
            reader = csv.DictReader(file)
            item_num = 1
            for product in reader:
                if item_num == product_index:
                # print(product)
                 product_name = product.get('name')
                item_num += 1
    except Exception as error1:
        print("failed to execute drink", error1)
    return product_name

# print(get_product_name(3))



# def update_status(order_status, product_index):
#     item_num = 1
#     products = []
#     with open('database/products.csv', 'r') as file:
#       reader = csv.DictReader(file)
#       for row in reader:    
#           if item_num == product_index:
#             row[5] = order_status
#           products.append(row)
#           item_num += 1

#     fieldnames = ['order_status', 'product_index']
#     with open('database/products.csv', 'w', newline="") as file:
#       write = csv.DictWriter(file, fieldnames=fieldnames)
#       write.writeheader()
#       write.writerows(products)

# update_status("on its way", 1)
