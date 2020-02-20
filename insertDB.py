#Module to be install 
#1. pip install xlrd
#2. pip install mysql-connector-python


"""
Database operation need to perform first

create database chamu;
use chamu;
create table tanmay(fname varchar(50),lname varchar(50), id int(3), address varchar(50));
"""



import xlrd
import dbConnection


#Open the workbook and define the worksheet
#try.xlsx is the name of your exel file
book = xlrd.open_workbook("try.xlsx")
sheet = book.sheet_by_name("Sheet1")

#this function create connection to database if succesful then connect else give error
database=dbConnection.connect()
# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

#this function perform insertion query to database
dbConnection.insert(cursor,book,sheet)
# Close the cursor
cursor.close()
# Commit the transaction
database.commit()
# Close the database connection
database.close()
