from calendar import c
from tkinter.tix import Tree
from turtle import title
import matplotlib.pyplot as plt 
import numpy as np
import DbOperations

#get data for pie chart from database
def getPieChartValues(cat):
        pieConn=DbOperations.openDbConnection()
        pieCursor=pieConn.cursor()
        getValuesQuery=("select medicinename, sum(quantity) as 'Total Stock' from meds_db where category='"+cat+"' group by medicinename")
        pieCursor.execute(getValuesQuery)
        pieList=pieCursor.fetchall()
        DbOperations.closeDbConnection(pieConn)
        return pieList

#get data for pie chart from database
def getPieChartValuesByCat():
        pieConn=DbOperations.openDbConnection()
        pieCursor=pieConn.cursor()
        getValuesQuery=("select category, sum(quantity) as 'Total Stock' from meds_db group by category")
        pieCursor.execute(getValuesQuery)
        pieList=pieCursor.fetchall()
        DbOperations.closeDbConnection(pieConn)
        return pieList

def plotMedicineChart(cat):
        list=getPieChartValues(cat)
        pieChartLabels=[]
        pieChartValues=[]
        for i in list:
                pieChartLabels.append(i[0])
                pieChartValues.append(i[1])

        pieObject = np.array(pieChartValues)

        plt.title("VMS Stock Available in " + cat)
        plt.pie(pieObject, labels = pieChartLabels, autopct='%1.1f%%',center=True)
        plt.show()

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

# Test code
# plotMedicineChart('ENT')
