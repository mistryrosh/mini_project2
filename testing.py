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



def add_drink(product):
    try:
        with open("database.product.txt" "a") as drinks_list:
            drinks_list.writelines()
    except Exception as error1:
        print("failed to add product")

add_drink("tea" "\n")