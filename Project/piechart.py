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

def plotChart(cat):
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


plotChart('ENT')
plotChart('Ophthalmic')
plotChart('Diabetes')
plotChart('PainKillers')