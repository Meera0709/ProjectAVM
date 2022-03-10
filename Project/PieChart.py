from turtle import title
import matplotlib.pyplot as plt 
import numpy as np
import DBOperations

# get data for pie chart from database by category
def getPieChartValues(cat):
        pieConn=DBOperations.openDbConnection()
        pieCursor=pieConn.cursor()
        getValuesQuery=("select medicinename, sum(quantity) as 'Total Stock' from meds_db where category='"+cat+"' group by medicinename")
        pieCursor.execute(getValuesQuery)
        pieList=pieCursor.fetchall()
        DBOperations.closeDbConnection(pieConn)
        return pieList

# get data for pie chart from database
def getPieChartValuesByCat():
        pieConn=DBOperations.openDbConnection()
        pieCursor=pieConn.cursor()
        getValuesQuery=("select category, sum(quantity) as 'Total Stock' from meds_db group by category")
        pieCursor.execute(getValuesQuery)
        pieList=pieCursor.fetchall()
        DBOperations.closeDbConnection(pieConn)
        return pieList

# display pie chart for stock according to category
def plotMedicineChart(cat):
        list=getPieChartValues(cat)
        pieChartLabels=[]
        pieChartValues=[]
        for i in list:
                pieChartLabels.append(i[0])
                pieChartValues.append(i[1])

        pieObject = np.array(pieChartValues)

        plt.title("VMS Stock Available in " + cat)
        plt.pie(pieObject, labels = pieChartLabels, autopct='%1.1f%%')
        plt.show()

# display overall pie chart for stock
def plotCategoryChart():
        list=getPieChartValuesByCat()
        pieChartLabels=[]
        pieChartValues=[]
        for i in list:
                pieChartLabels.append(i[0])
                pieChartValues.append(i[1])

        pieObject = np.array(pieChartValues)

        plt.title("VMS Stock Available")
        plt.pie(pieObject, labels = pieChartLabels, autopct='%1.1f%%')
        plt.show()
