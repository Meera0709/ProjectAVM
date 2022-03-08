import mysql.connector

#Function to open a database connection for query execution
def openDbConnection():
    try:
            dbConnection=mysql.connector.connect(host="localhost",user="root",password="0410",database="project")
            return dbConnection
    except mysql.connector.Error as sqlerror:
            print("DB error {}".format(sqlerror))

#Function to close the database connection after query execution
def closeDbConnection(dbConnection):
    try:
            dbConnection.close()       
    except mysql.connector.Error as sqlerror:
            print("DB error {}".format(sqlerror))
