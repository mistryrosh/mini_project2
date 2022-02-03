# def add_drinks(drink):
#     try:
#         with open("database/products.txt", "a") as drinks_list:
#             drinks_list.write(drink)     
#     except Exception as error1:
#         print("failed to add drink: ", error1 )

# add_drinks("orange juice\n")


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
#     product = product + "\n"
#     try:
#         with open("database/products.txt", "r") as drinks_list:
#             new_list = drinks_list.readlines()
#             for item in new_list:
#                 if item == product:
#                     new_list.remove(item)
#                     print(item)
#         try:
#             with open("database/products.txt", "w") as list_drinks:
#                 list_drinks.writelines(new_list)
#         except Exception as error1:
#             print("failed to write")
                            
#     except Exception as error1:
#         print("failed to read prodcuts: ", error1 )

# delete_item("apple juice")

# def update_item(drink):
#     drink = drink + "\n"
#     try:
#         with open("database/products.txt", "r") as drinks_list:
#             new_list = drinks_list.readlines()
#             for item in new_list:
#                 if item == drink:
#                     new_list.update(item)
#                     print(item)
#         try:
#             with open("database/products.txt", "w") as list_drinks:
#                 list_drinks.writelines(new_list)
#         except Exception as error1:
#             print("failed to write")
                            
#     except Exception as error1:
#         print("failed to read prodcut: ", error1 )

# update_item("tea")


# def update_item():

        
# elif user_input == 4:
#         old_drinks = input("which item would you like to update?: ")
#         new_drinks = input(f"What would like to replace {old_drinks} with?: ")
#         index_d = drinks_menu.index(old_drinks)
#         update_drinks(index_d, new_drinks) 
#     else:
#         print("Sorry, you are unable to proceed any further")