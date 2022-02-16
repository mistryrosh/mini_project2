
main_menu = '''
Menu Menu
0:Exit app
1.Add new product
2.View menu
3.Update/replace product 
4.Delet/Remove product "\n" 
'''

def a_cafe():   
        print(main_menu)
        user_input = int(input("welcome to A_cafe. Please select what option you would like to proceed with : "))
        if user_input == 0:
            print("please return to main menu")

        elif user_input == 1:
            new_product = input("please enter the name of the new item you would like to enter to the list : ")
            with open("database/products2.txt", 'a') as file:
                file.write(new_product + "\n")
        
        elif user_input == 2:
            with open("database/products2.txt", 'r') as file:
                view_menu = file.readlines()
                for products in view_menu:
                    print(products.replace("\n", ""))

        elif user_input == 3:
            old_product = input("which item would you like to update?: ")
            new_product = input(f"what would you like to replace {old_product} with?: ")
            old_product = old_product + "\n"
            with open("database/products2.txt", "r") as file:
                product_menu = file.readlines()
                # print(product_menu)
                for products in product_menu:
                    if products == old_product:
                        item_num = product_menu.index(products)
                        product_menu[item_num] = new_product + "\n"
                        with open("database/products2.txt", "w") as file:
                            file.writelines(product_menu)
            with open("database/products2.txt", 'r') as file:
                view_menu = file.readlines()
                for products in view_menu:
                    print(products.replace("\n", ""))

        elif user_input == 4:
            product_to_delete = input("what item would you like to delete?: ")
            product_to_delete = product_to_delete + "\n"
            with open("database/products2.txt", "r") as file:
                product_menu = file.readlines()
                for products in product_menu:
                    if products == product_to_delete:
                        item_num = product_menu.index(products)
                        del product_menu[item_num]
                        with open("database/products2.txt", "w") as file:
                            file.writelines(product_menu)
            with open("database/products2.txt", 'r') as file:
                view_menu = file.readlines()
                for products in view_menu:
                    print(products.replace("\n", ""))

a_cafe()









# update item

            

        # elif user_input == 4:
        #     product_to_delete = input("what item would you like to delete?: ")
        #     with open("database/products2.txt", "r") as file:
        #         product_menu = file.readlines()
        #         products.remove(product_menu)
        #         for items in products:
        #             print(product_menu)

# update item
        # elif user_input == 3:
        #     old_product = input("which item would you like to update?: ")
        #     new_product = input(f"what would you like to replace {old_product} with?: ")
        #     with open("database/products2.txt", "a+") as file:
        #         product_menu = file.writelines()
        #         product_num = product_menu.index(old_product)
        #         product_menu[product_num] = new_product
        #         for items in product_menu:
        #             print(items)

        
# update/replace with new product
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

# old_item = "mocha"
# new_item = "latte"
# update_item(old_item, new_item)


# delete item
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
                         



            






















