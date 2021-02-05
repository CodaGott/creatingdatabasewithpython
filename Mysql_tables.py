from dotenv import load_dotenv
import os
import mysql.connector
load_dotenv()
my_database_name = os.getenv("database_name")
my_database_password = os.getenv("password")
my_database_host = os.getenv("host")
my_database_user = os.getenv("user")
my_database_database = os.getenv("database")
my_database = None

my_database = mysql.connector.connect(
        host=my_database_host,
        user=my_database_user,
        password=my_database_password,
        database=my_database_name
    )

my_cursor = my_database.cursor()

# my_cursor.execute("CREATE TABLE if not exists Customer(customerid INT AUTO_INCREMENT PRIMARY KEY not null, "
#                   "firstname VARCHAR(55) not null ,lastname VARCHAR(55) not null, middlename varchar(55),"
#                   " dateofbirth DATE not null,occupation VARCHAR(255) not null )")

# my_cursor.execute("CREATE TABLE if not exists Account(AccountNumber INT(10) PRIMARY KEY not null, customerid INT,"
#                   "AccountType VARCHAR(20) not null ,AccountStatus VARCHAR(20) not null, AccountOpeningDate Date),"
#                   "not null FOREIGN KEY (customerid) REFERENCES Customer(customerid)")


my_cursor.execute("CREATE TABLE if not exists Account(accountNumber integer not null auto_increment,"
                  "customerId INT not null,"
                  "AccountType varchar(20),"
                  "AccountStatus varchar(30),"
                  "AccountOpeningDate DATE default (current_date),"
                  "constraint account_pk primary key(accountNumber),"
                  "constraint account_fk foreign key(customerId) references Customer(customerId)")