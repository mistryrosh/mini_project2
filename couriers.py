import db_connection as db
# from APP_FILES.couriers import get_courier_name

def menu():
    
    Main_Menu = '''
    [0] To exit app
    [1] To view couriers list
    [2] To add new couriers
    [3] To update/replace courier 
    [4] To Delete/Remove courier "\n" '''

    print(Main_Menu)

#add to couriers table
def add_courier(name, phone_num):
    try:
        with db.connection.cursor() as cursor:
            sql = "INSERT INTO couriers_table (courier_name, courier_phone_num) VALUES (%s, %s)"
            val = (name, phone_num)
            cursor.execute(sql,val)
    except Exception as e:         
        print('------------ FAILED TO ADD COURIER: ===>', e)        
    else:
        print(f'\n********************* NEW COURIER HAS SUCCESSFULLY BEEN ADDED *********************\n') 
        db.connection.commit()

#view couriers table
def view_courier():
    try:
        with db.connection.cursor() as cursor:
            sql = "SELECT * FROM couriers_table"
            cursor.execute(sql)
    except Exception as e:         
        print('------------ FAILED TO FETCH RECORDS: ===>', e)
    else:
        # Gets all records from the database
        fetched_rows = cursor.fetchall()

        # iterate through the fetched records(rows) and display them
        for fetch_row in fetched_rows:
            print(fetch_row[0], fetch_row[1], fetch_row[2])

#update couriers table
def update_courier(courier_name, courier_phone_num, courier_index):
    try:
        with db.connection.cursor() as cursor:
            sql = '''UPDATE couriers_table
            SET courier_name = %s, courier_phone_num = %s
            WHERE courier_id = %s'''
            val = (courier_name, courier_phone_num, courier_index)
            cursor.execute(sql,val)
    except Exception as e:         
        print('------------ FAILED TO ADD PRODUCT: ===>', e)        
    else:
        print(f' \n********************* COURIER HAS SUCCESSFULLY BEEN UPDATED *********************\n') 
        db.connection.commit()

#delete from couriers table
def delete_courier(courier_index):
    try:
        with db.connection.cursor() as cursor:
            sql = "DELETE FROM couriers_table WHERE courier_id = %s"
            val = (courier_index,)
            cursor.execute(sql,val)
    except Exception as e:         
        print('------------ FAILED TO ADD COURIER: ===>', e)        
    else:
        print(f'\n********************* COURIER HAS SUCCESSFULLY BEEN DELETED *********************\n') 
        db.connection.commit()
