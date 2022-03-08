import csv
import DbOperations



from turtle import window_height, window_width
def validateDOByear(date):
    if date.isnumeric():
        if int(date)<=2012 and int(date)>=1920:
            return True
    return False

def validateNull(input):
    if input:
        return True
    return False

def validateMobile(mobile):
    if mobile.isnumeric():
        if len(mobile)==10:
            return True
    return False

def validateDays(days):
    if int(days)<=30:
        return True
    return False

def validateInt(num):
    if num.isnumeric():
        return True
    return False
    
def validateCb(cbList):
    if any(cbList):
        return True
    return False
           
dict_medcat={}
f=open("medicine.csv","r")
reader=csv.reader(f)
for row in reader:
    if row!=[]:
        if row[0] not in dict_medcat:
            dict_medcat[row[0]]=[row[1]]
        else:
            dict_medcat[row[0]].append(row[1])
f.close()

def centerwindow(root, windowWidth,windowHeight):
    window_sw = root.winfo_screenwidth()
    window_sh = root.winfo_screenheight()
    
    # Gets both half the screen width/height and window width/height
    x = (window_sw/2) - (windowWidth/2)
    y = (window_sh/2) - (windowHeight/2)
    
    # Positions the window in the center of the page.
    root.geometry('%dx%d+%d+%d' % (windowWidth,windowHeight,x,y))


def validate(P):
    if len(P)==0 or len(P)<=10 and P.isdigit():
        return True
    else:
        return False 

def validate_year(P):
    if len(P)==0 or len(P)<=4 and P.isdigit():
        return True
    else:
        return False 

def refill_validate(mob):
    print("inside refill_val")
    RConn=DbOperations.openDbConnection()
    RCursor=RConn.cursor()
    RQuery="SELECT MobileNumber from PatientDetails where MobileNumber="+mob
    RCursor.execute(RQuery)
    RList=RCursor.fetchall()
    DbOperations.closeDbConnection(RConn)
    if len(RList)>0:
        return True
    else:
        return False