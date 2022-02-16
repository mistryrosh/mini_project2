drinks_menu = ["coffee", "hot chocolate", "latte", "flat white", "espresso", "chai latte", "mocha"]

main_menu = '''----- main menu --------
0. Exit
1. Drinks menu
2. Add new drinks
3. Delete/remove drink
4. Update drinks menu
-----------------'''

def new_item(product):
    drinks_menu.append(product)
    item_num = 1
    print("\n***********************New Drinks********************************\n")
    for item in drinks_menu:
        print(f"{item_num}. {item}")
        item_num += 1
    print("\n*******************************************************\n")

def update_drinks(old_drink, new_drink):
    drinks_menu[old_drink] = [new_drink]
    item_num = 1
    print("\n***********************New Drinks********************************\n")
    for item in drinks_menu:
        print(f"{item_num}. {item}")
        item_num += 1
    print("\n*******************************************************\n")

def remove_item(product):
    drinks_menu.remove(product)
    item_num = 1
    print("\n***********************New Drinks********************************\n")
    for item in drinks_menu:
        print(f"{item_num}. {item}")
        item_num += 1
    print("\n*******************************************************\n")


def start_A_cafe_app(user_input):
    if user_input == 0:
        print("Please return to main menu")
    elif user_input == 1:
        item_num = 1
        print("\n***********************Drinks********************************\n")
        for item in drinks_menu:
            print(f"{item_num}. {item}")
            item_num += 1
        print("\n*******************************************************\n")
    elif user_input == 2:
        get_item = input("please enter new drinks item: ")
        new_item(get_item)
    elif user_input == 3:
        old_drinks = input("which item would you like to update?: ")
        new_drinks = input(f"What would like to replace {old_drinks} with?: ")
        index_d = drinks_menu.index(old_drinks)
        update_drinks(index_d, new_drinks) 
    elif user_input == 4:
         get_item = input("what item would you like to remove: ")
         remove_item(get_item)
    else:
        print("Sorry, you are unable to proceed any further")


while True:
    print(main_menu)
    start_program = int(input("welcome to A_cafe. Please select from the menu what you would like to do : "))
    start_A_cafe_app(start_program)



