
# main_menu = '''
# Menu Menu
# 1.View Menu
# 2.Add new product
# 3.Update/replace product 
# 4.Delet/Remove product '''

# #view menu
# def products_menu():
#     try:
#         with open("database/products2.txt", "r") as product_item:
#             product_menu = product_item.readlines()
#             for products in product_menu:
#                 print(products.replace("\n", ""))
#     except Exception as error1:
#         print("failed to execute drink", error1)


user_input = int(input("welcome to A_cafe. Please select what option you would like to proceed with : "))
if user_input == 1:
    file = open("database/products2.txt", 'r')
    products_list = file.readlines()
    print(products_list)


# def product():
#     with open("database/products2.txt", "r"):
#         products = product_menu.readline()
#         for product in products_menu:
#             print(product)


# products_menu()

# add item
# def add_item(item):
#     try:
#         with open("database/products2.txt", "a") as product_item:
#             product_item.write(item + "\n")
#     except Exception as error1:
#         print("failed to execute drink", error1)

# item = "mocha"
# add_item(item)



# Use the below list to write all names to a file where each name is on a new line.


# file = open("people.txt", "r")
# students = file.read()
# persons = students.split()
# for person in persons:
#     print(person)

# with open()












