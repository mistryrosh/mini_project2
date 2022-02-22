import db_connection as db
# from APP_FILES.products import get_product_name

def menu():

    main_menu = '''
    [0] To return to Main Menu
    [1] To view Menu
    [2] To add new product
    [3] To update/replace product 
    [4] To Delete/Remove product "\n" '''

    print(main_menu)

#add to products table
def add_item(name, price):
    try:
        with db.connection.cursor() as cursor:
            sql = "INSERT INTO products_table (product_name, product_price) VALUES (%s, %s)"
            val = (name, price)
            cursor.execute(sql,val)
    except Exception as e:         
        print('------------ FAILED TO ADD PRODUCT: ===>', e)        
    else:
        print(f'\n********************* PRODUCT HAS SUCCESSFULLY BEEN ADDED *********************\n') 
        db.connection.commit()


def products_menu():
    try:
        with db.connection.cursor() as cursor:
            sql = "SELECT * FROM products_table"
            cursor.execute(sql)
    except Exception as e:         
        print('------------ FAILED TO FETCH RECORDS: ===>', e)
    else:
        # Gets all records from the database
        fetched_rows = cursor.fetchall()

        # iterate through the fetched records(rows) and display them
        for fetch_row in fetched_rows:
            print(fetch_row[0], fetch_row[1], fetch_row[2])


def update_item(product_name, product_price, product_index):
    try:
        with db.connection.cursor() as cursor:
            sql = '''UPDATE products_table
            SET product_name = %s, product_price = %s
            WHERE product_id = %s'''
            val = (product_name, product_price, product_index)
            cursor.execute(sql,val)
    except Exception as e:         
        print('------------ FAILED TO ADD PRODUCT: ===>', e)        
    else:
        print(f'\n********************* PRODUCT HAS SUCCESSFULLY BEEN UPDATED *********************\n') 
        db.connection.commit()


def delete_item(product_index):
    try:
        with db.connection.cursor() as cursor:
            sql = "DELETE FROM products_table WHERE product_id = %s"
            val = (product_index,)
            cursor.execute(sql,val)
    except Exception as e:         
        print('------------ FAILED TO ADD PRODUCT: ===>', e)        
    else:
        print(f'\n********************* PRODUCT HAS SUCCESSFULLY BEEN DELETED *********************\n') 
        db.connection.commit()
