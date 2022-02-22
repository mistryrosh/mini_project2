import db_connection as db
# import products
# import couriers

def menu():
  main_menu = '''
  [0] To return to main menu
  [1] To view order
  [2] To add to order
  [3] To update order status
  [4] To update an existing order
  [5] To Delete an order  "\n" '''
  
  print(main_menu)

#add to orders table
def add_to_order(product_list, name, address, phone_num, courier):
    item = "preparing"
    try:
        with db.connection.cursor() as cursor:
            sql = "INSERT INTO orders_table (customer_name, customer_address, customer_phone_num, order_status, courier_id) VALUES (%s, %s, %s, %s, %s)"
            val = (name, address, phone_num, item, courier)
            cursor.execute(sql,val)
    except Exception as e:         
        print('------------ FAILED TO ADD ORDER: ===>', e)        
    else:
        print(f'* YOUR ORDER HAS SUCCESSFULLY BEEN PLACED *') 
        db.connection.commit()
        id = cursor.lastrowid
        product_list = product_list.split(',')
        for product in product_list:
            product = int(product)
            try:
                with db.connection.cursor() as cursor:
                    sql = "INSERT INTO products_to_orders (order_id, product_id) VALUES (%s, %s)"
                    val = (id, product)
                    cursor.execute(sql,val)
                    db.connection.commit()
            except Exception as e:         
                    print('------------ FAILED TO ADD ORDER: ===>', e) 
        pass
                    


