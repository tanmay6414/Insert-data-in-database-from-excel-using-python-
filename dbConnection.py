#########################################
#@author : Tanmay Varade
########################################

import mysql.connector
from mysql.connector import errorcode

def connect():
	
	config = {
			  'user': 'root',
			  'password': 'root',
			  'host': '127.0.0.1',
			  'database': 'chamu',
			  'raise_on_warnings': True
			}
	try:
		# Establish a MySQL connection
		#give proper connection to your database
		database = mysql.connector.connect(**config)
		return database
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		    print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
		    print("Database does not exist")
		else:
		    print(err)


def insert(cursor,book,sheet):
	#this code prevent repitation of data in database
	search = "select max(id) from tanmay;"
	cursor.execute(search)
	myresult = cursor.fetchall()
	for i in myresult:
		a=i[0]


	# Create the INSERT INTO sql query
	#Before this query you need to create a databse and create one table in which you want to insert your data manually
	query = """INSERT INTO tanmay (fname, lname, id, address) VALUES (%s, %s, %s, %s)"""
	# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
	#In my table im not given any heading to the row thats why i started this loop from 0
	#but in your case  yor sheet has heading assign to it then your loop will be like that
	#####################################################

	#for r in range(1, sheet.nrows):

	######################################################
	search=0
	for r in range(0, sheet.nrows):
		fname= sheet.cell(r,0).value
		lname= sheet.cell(r,1).value
		id= str(sheet.cell(r,2).value)
		id=int(id[:1])
		address= sheet.cell(r,3).value
		if a==None:
			# Assign values from each row
			values = (fname, lname, id, address)
			# Execute sql Query
			cursor.execute(query, values)
			search=1
		else:
			a=int(a)
			if id>a:
				search=1
				values = (fname, lname, id, address)
				cursor.execute(query, values)
	if search==1:
		print("\n\nOperaytion perform successfully...!!!!\n\n")
	else:
		print("\n\nDatabase are up to date \nPlease try with new data....\n\n")

			
		
