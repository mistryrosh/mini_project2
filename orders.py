#update/replace with new product
# def update_item(old_item, new_item):
#     old_item = old_item + "\n"
#     try:
#         with open("database/products2.txt", "r") as product_item:
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

# old_item = "moacha"
# new_item = "latte"
# update_item(old_item, new_item)

#delete item
# def delete_item(old_item):
#     old_item = old_item + "\n"
#     try:
#         with open("database/products2.txt", "r") as product_item:
#             product_menu = product_item.readlines()
#             for products in product_menu:
#                 if products == old_item:
#                     item_num = product_menu.index(products)
#                     del product_menu[item_num]
#                     try:
#                         with open("database/products2.txt", "w") as product_item:
#                             product_item.writelines(product_menu)
#                             product_menu()
#                     except Exception as error1:
#                         print("failed to write to the file", error1)
#     except Exception as error1:
#         print("failed to execute drink", error1)

# delete_item("latte")