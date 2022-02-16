#2 drinks menu. Not going to use.
# hot_drinks = ["coffee", "hot chocolate", "Latte", "Flat white", "espresso", "Chai Latte", "Mocha", ]

# cold_drinks = ["Water", "Coke", "Coke Zero", "Freshly squeezed orange juice", " Frshly  squeezed apple juice"]

# def start_A_cafe_app(user_input):
#     if user_input == 0:
#         print("Return to main menu")
#     elif user_input == 1:
#         item_num = 1
#         print("\n***********************Hot Drinks********************************\n")
#         for item in hot_drinks:
#             print(f"{item_num}. {item}")
#             item_num += 1
#         else: 
#             item_num = 1
#             print("\n************************Cold Drinks*******************************\n")
#             for drinks in cold_drinks:
#                 print(f"{item_num}. {drinks}")
#                 item_num += 1
#         print("\n*******************************************************\n")
#     else:
#         print("sorry you can not go any futher")

# start_program = int(input("welcome to satrt_A_cafe. Please enter 0 to continue or 1 to terminate: "))
# start_A_cafe_app(start_program)

# fruits = ["apple", "banana", "pear"]
# new_fruit = input()
# fruits.append(new_fruit)

# print(fruits)

# drinks_menu = ["coffee", "hot chocolate", "Latte", "Flat white", "espresso", "Chai Latte", "Mocha"]
# new_drinks = input()
# drinks_menu.append(new_drinks)

# print(drinks_menu)


###############################################################################################################





# def user_login(username, password):
#     persons = {"roshni": 1234, "eddyvince": 123}
#     for user,passw in persons.items():
#         print(user,passw)
#         # if user == username and passw == password:
#         #     print("You have successfully logged in.")
#         # else:
#         #     print("Access denied")

# user_name = input("Enter username: ")
# pass_word = int(input(f"{user_name}, Please enter  your password: "))

# user_login(user_name, pass_word)

#############################################################################################################

# products txt functions - keeping here for now as created new one's

def add_drinks(drink):
    try:
        with open("database/products.txt", "a") as drinks_list:
            drinks_list.write(drink)     
    except Exception as error1:
        print("failed to add drink: ", error1 )

add_drinks("coffee" "\n")


# def drinks_menu():
#     try:
#         with open("database/products.txt", "r") as drinks_list:
#             new_list = drinks_list.readlines()
#             for item in new_list:
#                 print(item.replace("\n", ""))
#     except Exception as error1:
#         print("failed to read products: ", error1 )

# drinks_menu()


# def delete_item(product):
    # product = product + "\n"
    # try:
    #     with open("database/products.txt", "r") as drinks_list:
    #         new_list = drinks_list.readlines()
    #         for item in new_list:
    #             if item == product:
    #                 new_list.remove(item)
    #                 print(item)
    #     try:
    #         with open("database/products.txt", "w") as list_drinks:
    #             list_drinks.writelines(new_list)
    #     except Exception as error1:
    #         print("failed to write")
                            
    # except Exception as error1:
    #     print("failed to read prodcuts: ", error1 )



# update/replace with new product
# def update_item(old_item, new_item):
#     old_item = old_item + "\n"
#     try:
#         with open("database/products.txt", "r") as product_item:
#             product_menu = product_item.readlines()
#             for products in product_menu:
#                 if products == old_item:
#                     item_num = product_menu.index(products)
#                     product_menu[item_num] = new_item + "\n"
#                     try:
#                         with open("database/products2.txt", "w") as product_item:
#                             product_item.writelines(product_menu)
#                             product_menu()
#                     except Exception as error1:
#                         print("failed to write to the file", error1)
#     except Exception as error1:
#         print("failed to execute drink", error1)

# old_item = "tea"
# new_item = "apple juice"
# update_item(old_item, new_item)
