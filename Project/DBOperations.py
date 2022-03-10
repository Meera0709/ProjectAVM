import mysql.connector

# function to open the database connection returning a connection object
def openDbConnection():
    try:
            dbConnection=mysql.connector.connect(host="localhost",user="root",password="0410",database="project")
            return dbConnection
    except mysql.connector.Error as sqlerror:
            print("DB error {}".format(sqlerror))

# function to close the database connection 
def closeDbConnection(dbConnection):
    try:
            dbConnection.close()       
    except mysql.connector.Error as sqlerror:
            print("DB error {}".format(sqlerror))