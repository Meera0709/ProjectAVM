import matplotlib as plt 
import numpy as np
import DbOperations

#get data for pie chart from database
def getPieChartValues():
        pieConn=DbOperations.openDbConnection()
        pieCursor=pieConn.cursor()
        getValuesQuery=("select category, sum(quantity) as 'Total Stock' from meds_db group by category")
        pieCursor.execute(getValuesQuery)
        pieList=pieCursor.fetchall()
        DbOperations.closeDbConnection(pieConn)
        return pieList

print(np.version.version)