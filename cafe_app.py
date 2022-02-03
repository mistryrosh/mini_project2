products = ["coffee", "engliht tea", "hot chocolate", "water", "ornage juice", "coke"]

main_menu = '''
Menu Menu
0.Exit app
1.View Menu
2.Add new product
3.Update/replace product 
4.Delet/Remove product '''


def a_cafe(): 
    while True:
        print(main_menu)
        user_input = int(input("welcome to A_cafe. Please select what option you would like to proceed with : "))
        if user_input == 0:
            print("please return to main menu")
            break
        elif user_input == 1:
            for items in products:
                print(f"{items}")
        elif user_input == 2:
            new_product = input("please enter the name of the new item you would like to enter in the list : ")
            products.append(new_product)
            for items in products:
                print(f"{items}")
        elif user_input == 3:
            old_product = input("which item would you like to update?: ")
            new_product = input(f"what would you like to replace {old_product} with?: ")
            product_num = products.index(old_product)
            products[product_num] = new_product
            for items in products:
                print(f"{items}")
        elif user_input == 4:
            product_to_delete = input("what item would you like to delete?: ")
            products.remove(product_to_delete)
            for items in products:
                print(f"{items}")
            # del list[index] this is anotehr way to remove an item

a_cafe()

