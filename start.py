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
            print('\n********************* You have successfully exited the app *********************\n')
            break
        elif user_input == 1: #this is for products
            while True:
                products.menu()
                customer_input = int(input('What would you like to do?: '))
                if customer_input == 0: #return to main menu
                    print()
                    print('\n********************* You have successfully returned to main menu *********************\n')
                    break
                elif customer_input == 1: #view product
                    print()
                    products.products_menu()
                elif customer_input == 2: #add item
                    product_name = input('Enter new prodct?: ') #capture customer input
                    product_price = float(input('Enter item price: '))
                    products.add_item(product_name, product_price) #pass the input variable(customer_input) as an argument
                    # products.products_menu() #call menu with new item
                elif customer_input == 3: #update item
                    print()
                    products.products_menu()
                    print()
                    product_index = int(input('what item would you like to update?: '))
                    update_product = input('please enter new item: ')
                    new_price = input('Enter item price: ')
                    print()
                    products.update_item(update_product, new_price, product_index)
                    products.products_menu()
                elif customer_input == 4: #delete item
                    print()
                    products.products_menu()
                    print()
                    delete_item = int(input('what item would you like to delete?: '))
                    products.delete_item(delete_item)
                    products.products_menu()
           

        elif user_input == 2: #This is for couriers
            while True:
                couriers.menu()
                customer_input = int(input('Welcome to A_cafe. Please choose an option to proceed: '))
                if customer_input == 0: #return to main menu
                    print('\n********************* You have successfully returned to main menu *********************\n')
                    break
                elif customer_input == 1: #view couriers
                    print()
                    couriers.view_courier()
                elif customer_input == 2: #add new courier
                    new_courier = input('Enter the name of the new courier?: ') #capture customer input
                    courier_phone_num = input('Enter courier phone number: ')
                    print()
                    couriers.add_courier(new_courier, courier_phone_num) #pass the input variable(customer_input) as an argument            
                elif customer_input == 3: #update courier
                    print()
                    couriers.view_courier()
                    print()
                    courier_index = int(input('which courier would you like to update?: '))
                    new_courier = input('please enter the name of the new courier: ')
                    phone_num = input('Enter courier phone num: ')
                    print()
                    couriers.update_courier(new_courier, phone_num, courier_index)
                    couriers.view_courier()
                elif customer_input == 4:
                    print()
                    couriers.view_courier()
                    print()
                    delete_courier = int(input('Which courier would you like to delete?: '))
                    print()
                    couriers.delete_courier(delete_courier)
                    couriers.view_courier()


        elif user_input == 3: #This is for orders
            while True:
                orders.menu()
                customer_input = int(input('Welcome to A_cafe. Please choose an option to proceed?: '))
                if customer_input == 0:
                    print('\n********************* You have successfully returned to main menu *********************\n')
                    break
                elif customer_input == 1:
                    orders.view_order()
                elif customer_input == 2: #add to order
                    print()
                    products.products_menu()
                    print()
                    pick_product = input('What item would you like to add?: ')
                    customer_name = input('Please enter your full name: ') #capture customer input
                    customer_address = input('Please enter your address: ')
                    customer_phone_num = input('Please enter your phone number: ')
                    print()
                    couriers.view_courier()
                    print()
                    pick_courier = int(input('What courier would you you like to pick: '))
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