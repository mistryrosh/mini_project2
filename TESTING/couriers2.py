# main_menu = '''
# Menu Menu
# 0:Exit app
# 1.View couriers list
# 2.Add new couriers
# 3.Update/replace courier 
# 4.Delet/Remove courier "\n" '''

# def a_cafe():   
#         print(main_menu)
#         user_input = int(input("welcome to A_cafe. Please select what option you would like to proceed with : "))
#         if user_input == 0:
#             print("please return to main menu")

#         elif user_input == 1:
#             new_courier = input("please enter the name of the new courier you would like to enter to the list : ")
#             with open("database/couriers.txt", 'a') as file:
#                 file.write(new_courier + "\n")
        
#         elif user_input == 2:
#             with open("database/couriers.txt", 'r') as file:
#                 view_courier = file.readlines()
#                 for products in view_courier:
#                     print(products.replace("\n", ""))
       
#         elif user_input == 3:
#             with open("database/couriers.txt", 'r') as file:
                
        

# a_cafe()