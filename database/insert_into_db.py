import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host = host,
    user = user,
    password = password,
    database = database
)

# A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
cursor = connection.cursor()

#Add code here to insert a new record
# sql = "INSERT INTO person (first_name, last_name, age, email) VALUES (%s, %s,%s,%s)"
# val = [("John", "Highway",100,'jack@ufc.con')]
# cursor.executemany(sql,val)

#products table
sql = "INSERT INTO products_table (product_name, product_price) VALUES (%s, %s)"
val = ("coffee", "2.99","mocha")
cursor.execute(sql,val)



connection.commit()
cursor.close()
connection.close()