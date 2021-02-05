from dotenv import load_dotenv
import os
import mysql.connector
load_dotenv()
db_name = os.getenv("databasename")
password = os.getenv("password")
print(db_name)

def creating_of_database():

    my_database = mysql.connector.connect(
        host="localhost",
        user='greatchidozie',
        password='material4U'
    )

    mycursor = my_database.cursor()

    mycursor.execute("CREATE DATABASE if not exists BankDataBase")

    mycursor = my_database.cursor()

    mycursor.execute("SHOW DATABASES")

    mycursor.execute("CREATE TABLE if not exists customer(firstName VARCHAR(100),"
                     "lastName VARCHAR(100)")

# def database_exist():
#     my_database = mysql.connector.Connect(
#         host="localhost",
#         user='greatchidozie',
#         password='material4U'
#     )
#     mycursor = BankDataBase.cursor()
#
#     mycursor.execute("SHOW DATABASES")
#
#     for x in mycursor:
#         print(x)

if __name__ == "__main__":
    creating_of_database()