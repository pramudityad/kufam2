import mysql.connector
from mysql.connector import Error
import numpy

# try:
# 	connection = mysql.connector.connect(host='localhost',
# 										 database='kufarm',
# 										 user='root',
# 										 password='root')
# 	if connection.is_connected():
# 		db_Info = connection.get_server_info()
# 		print("Connected to MySQL Server version ", db_Info)
# 		cursor = connection.cursor()
# 		cursor.execute("select database();")
# 		record = cursor.fetchone()
# 		statusDB = True
# 		print("You're connected to database: ", record)    
# except Error as e:
# 	print("Error while connecting to MySQL", e)
# 	statusDB = False
# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

connection = mysql.connector.connect(host='localhost',
										 database='kufarm',
										 user='root',
										 password='root')

def getTrainData():
	try:
		connection
		if connection.is_connected():
			cursor = connection.cursor()
			sql = "SELECT temp, hump, ts from trainingset"			
			cursor.execute(sql)
			myresult = cursor.fetchall()
			data = numpy.array(myresult)
			inp = data[:,0:2]
			out = data[:,2]
			# cursor.close()
			# connection.close()
	except Exception :
		print('error in getTrainData')
	finally:
	    if (connection.is_connected()):
	        cursor.close()
	        connection.close()
	        print("MySQL connection is closed")
	return inp, out


def savetoDB(temp, hum, ts):	
	try:
		connection
		if connection.is_connected():			
			cursor = connection.cursor()
			sql = "INSERT INTO trainingset (temp, hump, ts) VALUES (%s, %s, %s)"
			val = (float(temp), float(hum), float(ts))
			cursor.execute(sql, val)
			connection.commit()
			print(cursor.rowcount, "record(s) inserted.")
			# cursor.close()
			# connection.close()
	except Exception :
		print('error in savetoDB')
	finally:
	    if (connection.is_connected()):
	        cursor.close()
	        connection.close()
	        print("MySQL connection is closed")