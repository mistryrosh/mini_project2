import products
import couriers
import orders

def main_menu():
    menu = '''
    [1] For products
    [2] For couriers
    [3] For orders
    [0] To Exit
    '''
    print(menu)

def run_app():
    while True:
        main_menu()
        user_input = int(input('welcome to A_cafe. Please choose an option to proceed: '))

        if(user_input == 0):
            print('You have successfully exited the app: ')
            break
        elif user_input == 1: #this is for products
            while True:
                products.menu()
                customer_input = int(input('What would you like to do?: '))
                if customer_input == 0:
                    print('please return to main menu: ')
                    break
                elif customer_input == 1:
                    products.products_menu()
                elif customer_input == 2:
                    customer_input = input('What item would you like to add?: ') #capture customer input
                    products.add_item(customer_input) #pass the input variable(customer_input) as an argument
                    products.products_menu() #call menu with new item
                elif customer_input == 3:
                    customer_input = input('what item would you like to update?: ')
                    new_item = input('please enter new item: ')
                    products.update_item(customer_input, new_item)
                    products.products_menu()
                elif customer_input == 4:
                    customer_input = input('what item would you like to delete?: ')
                    products.delete_item(customer_input)
                    products.products_menu()
           

        elif user_input == 2: #This is for couriers
            while True:
                couriers.menu()
                customer_input = int(input('Welcome to A_cafe. Please choose an option to proceed: '))
                if customer_input == 0:
                    print('You have successfully exited the app: ')
                    break
                elif customer_input == 1:
                    couriers.view_courier()
                elif customer_input == 2:
                    customer_input = input('Which courier would you like to add?: ') #capture customer input
                    couriers.add_courier(customer_input) #pass the input variable(customer_input) as an argument
                    couriers.view_courier() #call menu with new item
                elif customer_input == 3:
                    customer_input = input('Which courier would you like to update?: ')
                    new_item = input('please enter new courier: ')
                    couriers.update_courier(customer_input, new_item)
                    couriers.view_courier()
                elif customer_input == 4:
                    customer_input = input('Which courier would you like to delete?: ')
                    couriers.delete_courier(customer_input)
                    couriers.view_courier()



        elif user_input == 3: # this is for orders
            while True:
                orders.menu()
                customer_input = int(input('Welcome to A_cafe. Please choose an option to proceed?: '))
                if customer_input == 0:
                    print('You have successfully exited the app: ')
                    break
                elif customer_input == 1:
                    orders.view_order()
                elif customer_input == 2: #add to order
                    products.products_menu()
                    pick_product = int(input('What item would you like to add?: '))
                    customer_name = input('Please enter your full name: ') #capture customer input
                    customer_address = input('Please enter your address: ')
                    customer_phone_num = input('Please enter your phone number: ')
                    couriers.view_courier()
                    pick_courier = int(input('Please select what courier you would like go with: '))
                    orders.add_to_order(pick_product, customer_name, customer_address, customer_phone_num, pick_courier) #pass the input variable(customer_input) as an argument
                    # orders.view_order() #call menu with new item
                elif customer_input == 3: #update existing order status
                    print()
                    orders.view_order()
                    print()
                    pick_order_to_update = int(input('Which order number would you like to update the status for?: '))
                    print()
                    new_status = input('what status would you like to update with?: ')
                    orders.update_order_status(new_status, pick_order_to_update) 
                elif customer_input == 4: #update existing order
                    print()
                    orders.view_order()
                    print()
                    pick_order_to_update = int(input('Which order number would you like to update?: '))
                    print()
                    products.products_menu()
                    print()
                    pick_new_item = int(input('What would you like to update your existing drink order with?: '))
                    print()
                    couriers.view_courier()
                    print()
                    pick_new_courier = int(input('Which courier would you like to update with?: '))
                    print()
                    customer_name = input('Please enter your full name: ')
                    customer_address = input('Please enter your address: ')
                    customer_phone_num = input('Please enter your phone number: ')
                    orders.update_existing_order(pick_new_item, customer_name, customer_address, customer_phone_num, pick_new_courier, pick_order_to_update) # need courier, order status and order id
                    orders.view_order()
                elif customer_input == 5:
                    orders.view_order()
                    delete_order = int(input('Which order would you like to delete?: '))
                    orders.delete_order_item(delete_order)
                    
run_app()