def menu():

    main_menu = '''
    [0] To return to Main Menu
    [1] To view Menu
    [2] To add new product
    [3] To update/replace product 
    [4] To Delet/Remove product "\n" '''

    print(main_menu)


# add item - working but not for coffee - also first item not showing on line 1 
def add_item(item):
    try:
        with open("database/products.txt", "a", newline="") as product_item:
            product_item.write(item + "\n")
    except Exception as error1:
        print("failed to execute drink", error1)

# add_item("orange juice")

# view menu - working
def products_menu():
    try:
        with open("database/products.txt", "r") as product_item:
            product_menu = product_item.readlines()
            item_num = 1
            for products in product_menu:
                print(f"{item_num}.", products.replace("\n", ""))
                item_num += 1
    except Exception as error1:
        print("failed to execute drink", error1)

# products_menu()


# update/replace with new product - working
def update_item(old_item, new_item):
    old_item = old_item + "\n"
    try:
        with open("database/products.txt", "r") as product_item:
            product_menu = product_item.readlines()
            for products in product_menu:
                if products == old_item:
                    item_num = product_menu.index(products)
                    product_menu[item_num] = new_item + "\n"
                    try:
                        with open("database/products.txt", "w") as product_item:
                            product_item.writelines(product_menu)
                            product_menu
                    except Exception as error1:
                        print("failed to write to the file:", error1)
                    else: 
                        original_item = old_item.replace("\n", "") 
                        new_item.replace("\n", "")
                        print(f'{original_item} has now been updated to {new_item}')
    except Exception as error1:
        print("failed to execute drink", error1)

# old_item = "water"
# new_item = "tea"
# update_item(old_item, new_item)

# delete item - working
def delete_item(old_item):
    old_item = old_item + "\n"
    try:
        with open("database/products.txt", "r") as product_item:
            product_menu = product_item.readlines()
            for products in product_menu:
                if products == old_item:
                    item_num = product_menu.index(products)
                    del product_menu[item_num]
                    try:
                        with open("database/products.txt", "w") as product_item:
                            product_item.writelines(product_menu)
                            product_menu
                    except Exception as error1:
                        print("failed to write to the file", error1)
    except Exception as error1:
        print("failed to execute drink", error1)

# delete_item("tea")

def get_product_name(product_id):
    product_name = " "
    try:
        with open("database/products.txt", "r") as product_item:
            product_menu = product_item.readlines()
            item_num = 1
            for products in product_menu:
                if item_num == product_id:
                    product_name = products.replace("\n", "")
                # print(f"{item_num}.", products.replace("\n", ""))
                item_num += 1
    except Exception as error1:
        print("failed to execute drink", error1)
    return product_name

# print(get_product_name(3))




############################################################################################################


# def start_A_cafe_app(user_input):
#     if user_input == 0:
#         print("Please return to main menu")
#     elif user_input == 1:
#         item_num = 1
#         print("\n***********************Drinks********************************\n")
#         for item in products_menu:
#             print(f"{item_num}. {item}")
#             item_num += 1
#         print("\n*******************************************************\n")


# print(main_menu)
# start_program = int(input("welcome to A_cafe. Please select from the menu what you would like to do : "))
# start_A_cafe_app(start_program)
