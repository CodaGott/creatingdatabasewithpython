from dotenv import load_dotenv
import os
import mysql.connector
load_dotenv()
my_database_name = os.getenv("database_name")
my_database_password = os.getenv("password")
my_database_host = os.getenv("host")
my_database_user = os.getenv("user")
my_database = None

def creating_of_database():

    my_database = mysql.connector.connect(
        host=my_database_host,
        user=my_database_user,
        password=my_database_password
    )
    print(my_database)

    my_cursor = my_database.cursor()

    my_cursor.execute("CREATE DATABASE if not exists BankAccountDataBase")

    my_cursor.execute("SHOW DATABASES")
    for db in my_cursor:
        print(db)

if __name__ == "__main__":
    creating_of_database()