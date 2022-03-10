from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import DBOperations
from Common import *
import mysql.connector

# function to get distinct rows based on category, medicinename, dosage and unit to be used in
# prescription refill window to handle duplicate data
def populate(mobile):
    RefillConn=DBOperations.openDbConnection()
    RefCursor=RefillConn.cursor()
    RefQuery="SELECT distinctrow Category, MedicineName,Dosage,Unit from patientPresc where MobileNumber="+mobile
    RefCursor.execute(RefQuery)
    RefList=RefCursor.fetchall()
    DBOperations.closeDbConnection(RefillConn)
    return RefList

# function to open the prescription window in NEW or REFILL mode
# to avoid redundant painting of the window
def openPrescription(mode,drugDispensingWindow,mobile):
    if (mode=="NEW"):
        dataList=[]
    else:
        #refill mode to get data for a given mobile number
        dataList=populate(mobile)
    # paint the window 
    paintPrescriptionWindow(drugDispensingWindow,mobile,dataList)

# function to paint the window in NEW or REFILL mode
def paintPrescriptionWindow(drugDispensingWindow,mobile,dataList):
    # open new window
    Presc=Toplevel(drugDispensingWindow)
    Presc.grab_set()
    Presc.title("MEDICINE PRESCRIPTION")
    Presc.configure(bg="lightgreen")
    centerwindow(Presc,500,300)
    Presc.resizable(0,0)

    # SNO
    SNO=Label(Presc,text="S.NO.",bg="lightgreen")
    SNO.grid(row=1,column=0)

    # CATEGORY
    CAT=Label(Presc,text="CATEGORY",bg="lightgreen")
    CAT.grid(row=1,column=1)

    # MED NAME
    DRUG=Label(Presc,text="MEDICINE NAME",bg="lightgreen")
    DRUG.grid(row=1,column=2)

    # DOSAGE
    DOSE=Label(Presc,text="DOSAGE",bg="lightgreen")
    DOSE.grid(row=1,column=3)

    # UNIT
    UNIT=Label(Presc,text="UNIT",bg="lightgreen")
    UNIT.grid(row=1,column=4)

    # TIMINGS
    M=Label(Presc,text="TIME OF DAY",bg="lightgreen")
    M.grid(row=1,column=5)

    # NO. OF DAYS
    DAYS=Label(Presc,text="DAYS",bg="lightgreen")
    DAYS.grid(row=1,column=6)

    for i in range(1,11):
        SNO1=Label(Presc,text=str(i),bg="lightgreen")
        SNO1.grid(row=i+1,column=0)
    
    cat_values=getCategoryValues()

    # Handle keyreleased event to populate medicine combobox based on the category 
    # combobox value selection 
    def getMedicinename1(event):
        value=event.widget.get()
        MEDICINE1.config(values=dict_medcat.get(value))

    def getMedicinename2(event):
        value=event.widget.get()
        MEDICINE2.config(values=dict_medcat.get(value))

    def getMedicinename3(event):
        value=event.widget.get()
        MEDICINE3.config(values=dict_medcat.get(value))

    def getMedicinename4(event):
        value=event.widget.get()
        MEDICINE4.config(values=dict_medcat.get(value))

    def getMedicinename5(event):
        value=event.widget.get()
        MEDICINE5.config(values=dict_medcat.get(value))

    def getMedicinename6(event):
        value=event.widget.get()
        MEDICINE6.config(values=dict_medcat.get(value))

    def getMedicinename7(event):
        value=event.widget.get()
        MEDICINE7.config(values=dict_medcat.get(value))

    def getMedicinename8(event):
        value=event.widget.get()
        MEDICINE8.config(values=dict_medcat.get(value))

    def getMedicinename9(event):
        value=event.widget.get()
        MEDICINE9.config(values=dict_medcat.get(value))

    def getMedicinename10(event):
        value=event.widget.get()
        MEDICINE10.config(values=dict_medcat.get(value)) 

    # category and medicine name combobox
    CATEGORY1=ttk.Combobox(Presc,values=cat_values,width=10,state="readonly")
    CATEGORY1.grid(row=2,column=1)
    CATEGORY1.bind('<<ComboboxSelected>>', getMedicinename1)
    MEDICINE1=ttk.Combobox(Presc,width=10,state="readonly")
    MEDICINE1.grid(row=2,column=2) 
    CATEGORY2=ttk.Combobox(Presc,values=cat_values,width=10, state="readonly")
    CATEGORY2.grid(row=3,column=1)
    CATEGORY2.bind('<<ComboboxSelected>>', getMedicinename2)
    MEDICINE2=ttk.Combobox(Presc,width=10,state="readonly")
    MEDICINE2.grid(row=3,column=2)
    CATEGORY3=ttk.Combobox(Presc,values=cat_values,width=10,state="readonly")
    CATEGORY3.grid(row=4,column=1)
    CATEGORY3.bind('<<ComboboxSelected>>', getMedicinename3)
    MEDICINE3=ttk.Combobox(Presc,width=10,state="readonly")
    MEDICINE3.grid(row=4,column=2)
    CATEGORY4=ttk.Combobox(Presc,values=cat_values,width=10,state="readonly")
    CATEGORY4.grid(row=5,column=1)
    CATEGORY4.bind('<<ComboboxSelected>>', getMedicinename4)
    MEDICINE4=ttk.Combobox(Presc,width=10,state="readonly")
    MEDICINE4.grid(row=5,column=2)
    CATEGORY5=ttk.Combobox(Presc,values=cat_values,width=10,state="readonly")
    CATEGORY5.grid(row=6,column=1)
    CATEGORY5.bind('<<ComboboxSelected>>', getMedicinename5)
    MEDICINE5=ttk.Combobox(Presc,width=10,state="readonly")
    MEDICINE5.grid(row=6,column=2)
    CATEGORY6=ttk.Combobox(Presc,values=cat_values,width=10,state="readonly")
    CATEGORY6.grid(row=7,column=1)
    CATEGORY6.bind('<<ComboboxSelected>>', getMedicinename6)
    MEDICINE6=ttk.Combobox(Presc,width=10,state="readonly")
    MEDICINE6.grid(row=7,column=2)
    CATEGORY7=ttk.Combobox(Presc,values=cat_values,width=10,state="readonly")
    CATEGORY7.grid(row=8,column=1)
    CATEGORY7.bind('<<ComboboxSelected>>', getMedicinename7)
    MEDICINE7=ttk.Combobox(Presc,width=10,state="readonly")
    MEDICINE7.grid(row=8,column=2)
    CATEGORY8=ttk.Combobox(Presc,values=cat_values,width=10,state="readonly")
    CATEGORY8.grid(row=9,column=1)
    CATEGORY8.bind('<<ComboboxSelected>>', getMedicinename8)
    MEDICINE8=ttk.Combobox(Presc,width=10,state="readonly")
    MEDICINE8.grid(row=9,column=2)
    CATEGORY9=ttk.Combobox(Presc,values=cat_values,width=10,state="readonly")
    CATEGORY9.grid(row=10,column=1)
    CATEGORY9.bind('<<ComboboxSelected>>', getMedicinename9)
    MEDICINE9=ttk.Combobox(Presc,width=10,state="readonly")
    MEDICINE9.grid(row=10,column=2)
    CATEGORY10=ttk.Combobox(Presc,values=cat_values,width=10,state="readonly")
    CATEGORY10.grid(row=11,column=1)
    CATEGORY10.bind('<<ComboboxSelected>>', getMedicinename10)
    MEDICINE10=ttk.Combobox(Presc,width=10,state="readonly")
    MEDICINE10.grid(row=11,column=2)

    DOSE1=Entry(Presc,width=7)
    DOSE1.grid(row=2,column=3)
    DOSE2=Entry(Presc,width=7)
    DOSE2.grid(row=3,column=3)
    DOSE3=Entry(Presc,width=7)
    DOSE3.grid(row=4,column=3)
    DOSE4=Entry(Presc,width=7)
    DOSE4.grid(row=5,column=3)
    DOSE5=Entry(Presc,width=7)
    DOSE5.grid(row=6,column=3)
    DOSE6=Entry(Presc,width=7)
    DOSE6.grid(row=7,column=3)
    DOSE7=Entry(Presc,width=7)
    DOSE7.grid(row=8,column=3)
    DOSE8=Entry(Presc,width=7)
    DOSE8.grid(row=9,column=3)
    DOSE9=Entry(Presc,width=7)
    DOSE9.grid(row=10,column=3)
    DOSE10=Entry(Presc,width=7)
    DOSE10.grid(row=11,column=3)

    UNITv1=StringVar(Presc)
    UNITv2=StringVar(Presc)
    UNITv3=StringVar(Presc)
    UNITv4=StringVar(Presc)
    UNITv5=StringVar(Presc)
    UNITv6=StringVar(Presc)
    UNITv7=StringVar(Presc)
    UNITv8=StringVar(Presc)
    UNITv9=StringVar(Presc)
    UNITv10=StringVar(Presc)

    UNIT1=Spinbox(Presc,values=("mg","ml"),textvariable=UNITv1,width=4)
    UNIT1.grid(row=2,column=4)
    UNIT2=Spinbox(Presc,values=("mg","ml"),textvariable=UNITv2,width=4)
    UNIT2.grid(row=3,column=4)
    UNIT3=Spinbox(Presc,values=("mg","ml"),textvariable=UNITv3,width=4)
    UNIT3.grid(row=4,column=4)
    UNIT4=Spinbox(Presc,values=("mg","ml"),textvariable=UNITv4,width=4)
    UNIT4.grid(row=5,column=4)
    UNIT5=Spinbox(Presc,values=("mg","ml"),textvariable=UNITv5,width=4)
    UNIT5.grid(row=6,column=4)
    UNIT6=Spinbox(Presc,values=("mg","ml"),textvariable=UNITv6,width=4)
    UNIT6.grid(row=7,column=4)
    UNIT7=Spinbox(Presc,values=("mg","ml"),textvariable=UNITv7,width=4)
    UNIT7.grid(row=8,column=4)
    UNIT8=Spinbox(Presc,values=("mg","ml"),textvariable=UNITv8,width=4)
    UNIT8.grid(row=9,column=4)
    UNIT9=Spinbox(Presc,values=("mg","ml"),textvariable=UNITv9,width=4)
    UNIT9.grid(row=10,column=4)
    UNIT10=Spinbox(Presc,values=("mg","ml"),textvariable=UNITv10,width=4)
    UNIT10.grid(row=11,column=4)

    Checkbutton11 = IntVar()
    Checkbutton12 = IntVar()
    Checkbutton13 = IntVar()
    Checkbutton14 = IntVar()

    FRAME1=Frame(Presc)
    M1=Checkbutton(FRAME1,variable=Checkbutton11,text='M',onvalue=1,offvalue=0,bg="lightgreen")
    A1=Checkbutton(FRAME1,variable=Checkbutton12,text='A',onvalue=1,offvalue=0,bg="lightgreen")
    E1=Checkbutton(FRAME1,variable=Checkbutton13,text='E',onvalue=1,offvalue=0,bg="lightgreen")
    N1=Checkbutton(FRAME1,variable=Checkbutton14,text='N',onvalue=1,offvalue=0,bg="lightgreen")

    M1.pack(side=LEFT)
    A1.pack(side=LEFT)
    E1.pack(side=LEFT)
    N1.pack(side=LEFT)
    FRAME1.grid(row=2,column=5)

    Checkbutton21 = IntVar()
    Checkbutton22 = IntVar()
    Checkbutton23 = IntVar()
    Checkbutton24 = IntVar()

    FRAME2=Frame(Presc)
    M2=Checkbutton(FRAME2,variable=Checkbutton21,text='M',onvalue=1,offvalue=0,bg="lightgreen")
    A2=Checkbutton(FRAME2,variable=Checkbutton22,text='A',onvalue=1,offvalue=0,bg="lightgreen")
    E2=Checkbutton(FRAME2,variable=Checkbutton23,text='E',onvalue=1,offvalue=0,bg="lightgreen")
    N2=Checkbutton(FRAME2,variable=Checkbutton24,text='N',onvalue=1,offvalue=0,bg="lightgreen")

    M2.pack(side=LEFT)
    A2.pack(side=LEFT)
    E2.pack(side=LEFT)
    N2.pack(side=LEFT)
    FRAME2.grid(row=3,column=5)

    Checkbutton31 = IntVar()
    Checkbutton32 = IntVar()
    Checkbutton33 = IntVar()
    Checkbutton34 = IntVar()

    FRAME3=Frame(Presc)
    M3=Checkbutton(FRAME3,variable=Checkbutton31,text='M',onvalue=1,offvalue=0,bg="lightgreen")
    A3=Checkbutton(FRAME3,variable=Checkbutton32,text='A',onvalue=1,offvalue=0,bg="lightgreen")
    E3=Checkbutton(FRAME3,variable=Checkbutton33,text='E',onvalue=1,offvalue=0,bg="lightgreen")
    N3=Checkbutton(FRAME3,variable=Checkbutton34,text='N',onvalue=1,offvalue=0,bg="lightgreen")

    M3.pack(side=LEFT)
    A3.pack(side=LEFT)
    E3.pack(side=LEFT)
    N3.pack(side=LEFT)
    FRAME3.grid(row=4,column=5)

    Checkbutton41 = IntVar()
    Checkbutton42 = IntVar()
    Checkbutton43 = IntVar()
    Checkbutton44 = IntVar()

    FRAME4=Frame(Presc)
    M4=Checkbutton(FRAME4,variable=Checkbutton41,text='M',onvalue=1,offvalue=0,bg="lightgreen")
    A4=Checkbutton(FRAME4,variable=Checkbutton42,text='A',onvalue=1,offvalue=0,bg="lightgreen")
    E4=Checkbutton(FRAME4,variable=Checkbutton43,text='E',onvalue=1,offvalue=0,bg="lightgreen")
    N4=Checkbutton(FRAME4,variable=Checkbutton44,text='N',onvalue=1,offvalue=0,bg="lightgreen")

    M4.pack(side=LEFT)
    A4.pack(side=LEFT)
    E4.pack(side=LEFT)
    N4.pack(side=LEFT)
    FRAME4.grid(row=5,column=5)

    Checkbutton51 = IntVar()
    Checkbutton52 = IntVar()
    Checkbutton53 = IntVar()
    Checkbutton54 = IntVar()

    FRAME5=Frame(Presc)
    M5=Checkbutton(FRAME5,variable=Checkbutton51,text='M',onvalue=1,offvalue=0,bg="lightgreen")
    A5=Checkbutton(FRAME5,variable=Checkbutton52,text='A',onvalue=1,offvalue=0,bg="lightgreen")
    E5=Checkbutton(FRAME5,variable=Checkbutton53,text='E',onvalue=1,offvalue=0,bg="lightgreen")
    N5=Checkbutton(FRAME5,variable=Checkbutton54,text='N',onvalue=1,offvalue=0,bg="lightgreen")

    M5.pack(side=LEFT)
    A5.pack(side=LEFT)
    E5.pack(side=LEFT)
    N5.pack(side=LEFT)
    FRAME5.grid(row=6,column=5)

    Checkbutton61 = IntVar()
    Checkbutton62 = IntVar()
    Checkbutton63 = IntVar()
    Checkbutton64 = IntVar()

    FRAME6=Frame(Presc)
    M6=Checkbutton(FRAME6,variable=Checkbutton61,text='M',onvalue=1,offvalue=0,bg="lightgreen")
    A6=Checkbutton(FRAME6,variable=Checkbutton62,text='A',onvalue=1,offvalue=0,bg="lightgreen")
    E6=Checkbutton(FRAME6,variable=Checkbutton63,text='E',onvalue=1,offvalue=0,bg="lightgreen")
    N6=Checkbutton(FRAME6,variable=Checkbutton64,text='N',onvalue=1,offvalue=0,bg="lightgreen")

    M6.pack(side=LEFT)
    A6.pack(side=LEFT)
    E6.pack(side=LEFT)
    N6.pack(side=LEFT)
    FRAME6.grid(row=7,column=5)

    Checkbutton71 = IntVar()
    Checkbutton72 = IntVar()
    Checkbutton73 = IntVar()
    Checkbutton74 = IntVar()

    FRAME7=Frame(Presc)
    M7=Checkbutton(FRAME7,variable=Checkbutton71,text='M',onvalue=1,offvalue=0,bg="lightgreen")
    A7=Checkbutton(FRAME7,variable=Checkbutton72,text='A',onvalue=1,offvalue=0,bg="lightgreen")
    E7=Checkbutton(FRAME7,variable=Checkbutton73,text='E',onvalue=1,offvalue=0,bg="lightgreen")
    N7=Checkbutton(FRAME7,variable=Checkbutton74,text='N',onvalue=1,offvalue=0,bg="lightgreen")

    M7.pack(side=LEFT)
    A7.pack(side=LEFT)
    E7.pack(side=LEFT)
    N7.pack(side=LEFT)
    FRAME7.grid(row=8,column=5)

    Checkbutton81 = IntVar()
    Checkbutton82 = IntVar()
    Checkbutton83 = IntVar()
    Checkbutton84 = IntVar()

    FRAME8=Frame(Presc)
    M8=Checkbutton(FRAME8,variable=Checkbutton81,text='M',onvalue=1,offvalue=0,bg="lightgreen")
    A8=Checkbutton(FRAME8,variable=Checkbutton82,text='A',onvalue=1,offvalue=0,bg="lightgreen")
    E8=Checkbutton(FRAME8,variable=Checkbutton83,text='E',onvalue=1,offvalue=0,bg="lightgreen")
    N8=Checkbutton(FRAME8,variable=Checkbutton84,text='N',onvalue=1,offvalue=0,bg="lightgreen")

    M8.pack(side=LEFT)
    A8.pack(side=LEFT)
    E8.pack(side=LEFT)
    N8.pack(side=LEFT)
    FRAME8.grid(row=9,column=5)

    Checkbutton91 = IntVar()
    Checkbutton92 = IntVar()
    Checkbutton93 = IntVar()
    Checkbutton94 = IntVar()

    FRAME9=Frame(Presc)
    M9=Checkbutton(FRAME9,variable=Checkbutton91,text='M',onvalue=1,offvalue=0,bg="lightgreen")
    A9=Checkbutton(FRAME9,variable=Checkbutton92,text='A',onvalue=1,offvalue=0,bg="lightgreen")
    E9=Checkbutton(FRAME9,variable=Checkbutton93,text='E',onvalue=1,offvalue=0,bg="lightgreen")
    N9=Checkbutton(FRAME9,variable=Checkbutton94,text='N',onvalue=1,offvalue=0,bg="lightgreen")

    M9.pack(side=LEFT)
    A9.pack(side=LEFT)
    E9.pack(side=LEFT)
    N9.pack(side=LEFT)
    FRAME9.grid(row=10,column=5)

    Checkbutton101 = IntVar()
    Checkbutton102 = IntVar()
    Checkbutton103 = IntVar()
    Checkbutton104 = IntVar()

    FRAME10=Frame(Presc)
    M10=Checkbutton(FRAME10,variable=Checkbutton101,text='M',onvalue=1,offvalue=0,bg="lightgreen")
    A10=Checkbutton(FRAME10,variable=Checkbutton102,text='A',onvalue=1,offvalue=0,bg="lightgreen")
    E10=Checkbutton(FRAME10,variable=Checkbutton103,text='E',onvalue=1,offvalue=0,bg="lightgreen")
    N10=Checkbutton(FRAME10,variable=Checkbutton104,text='N',onvalue=1,offvalue=0,bg="lightgreen")

    M10.pack(side=LEFT)
    A10.pack(side=LEFT)
    E10.pack(side=LEFT)
    N10.pack(side=LEFT)
    FRAME10.grid(row=11,column=5)

    DAYS1=Entry(Presc,width=5)
    DAYS1.grid(row=2,column=6)
    DAYS2=Entry(Presc,width=5)
    DAYS2.grid(row=3,column=6)
    DAYS3=Entry(Presc,width=5)
    DAYS3.grid(row=4,column=6)
    DAYS4=Entry(Presc,width=5)
    DAYS4.grid(row=5,column=6)
    DAYS5=Entry(Presc,width=5)
    DAYS5.grid(row=6,column=6)
    DAYS6=Entry(Presc,width=5)
    DAYS6.grid(row=7,column=6)
    DAYS7=Entry(Presc,width=5)
    DAYS7.grid(row=8,column=6)
    DAYS8=Entry(Presc,width=5)
    DAYS8.grid(row=9,column=6)
    DAYS9=Entry(Presc,width=5)
    DAYS9.grid(row=10,column=6)
    DAYS10=Entry(Presc,width=5)
    DAYS10.grid(row=11,column=6)

    # populate window with data in refill mode
    if len(dataList)>0:
        # append empty data for the remainder of the rows in the window 
        # based on the number of records returned
        for i in range (10-len(dataList)):
            dataList.append(['','','','mg',0,0,0,0,''])

        CATEGORY1.set(dataList[0][0])
        CATEGORY2.set(dataList[1][0])
        CATEGORY3.set(dataList[2][0])
        CATEGORY4.set(dataList[3][0])
        CATEGORY5.set(dataList[4][0])
        CATEGORY6.set(dataList[5][0])
        CATEGORY7.set(dataList[6][0])
        CATEGORY8.set(dataList[7][0])
        CATEGORY9.set(dataList[8][0])
        CATEGORY10.set(dataList[9][0])

        MEDICINE1.set(dataList[0][1])
        MEDICINE2.set(dataList[1][1])
        MEDICINE3.set(dataList[2][1])
        MEDICINE4.set(dataList[3][1])
        MEDICINE5.set(dataList[4][1])
        MEDICINE6.set(dataList[5][1])
        MEDICINE7.set(dataList[6][1])
        MEDICINE8.set(dataList[7][1])
        MEDICINE9.set(dataList[8][1])
        MEDICINE10.set(dataList[9][1])

        DOSE1.insert(END,dataList[0][2])
        DOSE2.insert(END,dataList[1][2])
        DOSE3.insert(END,dataList[2][2])
        DOSE4.insert(END,dataList[3][2])
        DOSE5.insert(END,dataList[4][2])
        DOSE6.insert(END,dataList[5][2])
        DOSE7.insert(END,dataList[6][2])
        DOSE8.insert(END,dataList[7][2])
        DOSE9.insert(END,dataList[8][2])
        DOSE10.insert(END,dataList[9][2])

        UNITv1.set(dataList[0][3])
        UNITv2.set(dataList[1][3])
        UNITv3.set(dataList[2][3])
        UNITv4.set(dataList[3][3])
        UNITv5.set(dataList[4][3])
        UNITv6.set(dataList[5][3])
        UNITv7.set(dataList[6][3])
        UNITv8.set(dataList[7][3])
        UNITv9.set(dataList[8][3])
        UNITv10.set(dataList[9][3])

    # function to handle prescription window submit clicked event
    def click_presc_submit():
    
        cat1=CATEGORY1.get()
        cat2=CATEGORY2.get()
        cat3=CATEGORY3.get()
        cat4=CATEGORY4.get()
        cat5=CATEGORY5.get()
        cat6=CATEGORY6.get()
        cat7=CATEGORY7.get()
        cat8=CATEGORY8.get()
        cat9=CATEGORY9.get()
        cat10=CATEGORY10.get()

        med1=MEDICINE1.get()
        med2=MEDICINE2.get()
        med3=MEDICINE3.get()
        med4=MEDICINE4.get()
        med5=MEDICINE5.get()
        med6=MEDICINE6.get()
        med7=MEDICINE7.get()
        med8=MEDICINE8.get()
        med9=MEDICINE9.get()
        med10=MEDICINE10.get()

        dose1=DOSE1.get()
        dose2=DOSE2.get()
        dose3=DOSE3.get() 
        dose4=DOSE4.get()
        dose5=DOSE5.get()
        dose6=DOSE6.get()
        dose7=DOSE7.get()
        dose8=DOSE8.get()
        dose9=DOSE9.get()
        dose10=DOSE10.get()

        unit1=UNIT1.get()
        unit2=UNIT2.get()
        unit3=UNIT3.get() 
        unit4=UNIT4.get()
        unit5=UNIT5.get()
        unit6=UNIT6.get()
        unit7=UNIT7.get()
        unit8=UNIT8.get()
        unit9=UNIT9.get()
        unit10=UNIT10.get()

        cb11=Checkbutton11.get()
        cb12=Checkbutton12.get()
        cb13=Checkbutton13.get()
        cb14=Checkbutton14.get()
        cb21=Checkbutton21.get()
        cb22=Checkbutton22.get()
        cb23=Checkbutton23.get()
        cb24=Checkbutton24.get()
        cb31=Checkbutton31.get()
        cb32=Checkbutton32.get()
        cb33=Checkbutton33.get()
        cb34=Checkbutton34.get()
        cb41=Checkbutton41.get()
        cb42=Checkbutton42.get()
        cb43=Checkbutton43.get()
        cb44=Checkbutton44.get()
        cb51=Checkbutton51.get()
        cb52=Checkbutton52.get()
        cb53=Checkbutton53.get()
        cb54=Checkbutton54.get()
        cb61=Checkbutton61.get()
        cb62=Checkbutton62.get()
        cb63=Checkbutton63.get()
        cb64=Checkbutton64.get()
        cb71=Checkbutton71.get()
        cb72=Checkbutton72.get()
        cb73=Checkbutton73.get()
        cb74=Checkbutton74.get()
        cb81=Checkbutton81.get()
        cb82=Checkbutton82.get()
        cb83=Checkbutton83.get()
        cb84=Checkbutton84.get()
        cb91=Checkbutton91.get()
        cb92=Checkbutton92.get()
        cb93=Checkbutton93.get()
        cb94=Checkbutton94.get()
        cb101=Checkbutton101.get()
        cb102=Checkbutton102.get()
        cb103=Checkbutton103.get()
        cb104=Checkbutton104.get()

        days1=DAYS1.get()
        days2=DAYS2.get()
        days3=DAYS3.get()
        days4=DAYS4.get()
        days5=DAYS5.get()
        days6=DAYS6.get()
        days7=DAYS7.get()
        days8=DAYS8.get()
        days9=DAYS9.get()
        days10=DAYS10.get()
        
        nlist=[[cat1,med1,dose1,unit1,cb11,cb12,cb13,cb14,days1],
        [cat2,med2,dose2,unit2,cb21,cb22,cb23,cb24,days2],
        [cat3,med3,dose3,unit3,cb31,cb32,cb33,cb34,days3],
        [cat4,med4,dose4,unit4,cb41,cb42,cb43,cb44,days4],
        [cat5,med5,dose5,unit5,cb51,cb52,cb53,cb54,days5],
        [cat6,med6,dose6,unit6,cb61,cb62,cb63,cb64,days6],
        [cat7,med7,dose7,unit7,cb71,cb72,cb73,cb74,days7],
        [cat8,med8,dose8,unit8,cb81,cb82,cb83,cb84,days8],
        [cat9,med9,dose9,unit9,cb91,cb92,cb93,cb94,days9],
        [cat10,med10,dose10,unit10,cb101,cb102,cb103,cb104,days10]]
        # row level data validation
        def validate2():
            flag=True
            for row in nlist:
                cbList=[row[4],row[5],row[6],row[7]]
                if validateNull(row[0]):
                    for cell in range(1,len(row)):
                        # skip all check boxes
                        if cell in [4,5,6,7]:
                            continue
                        else:
                            # prompt to fill the remaining data 
                            if validateNull(row[cell])==False:
                                messagebox.showwarning(message="Fill remaining details of Row Number "+str(nlist.index(row)+1))
                                flag=False
                                break
                    if validateNull(row[2]) and validateNull(row[-1]):    
                        if validateInt(row[2])==False:
                            messagebox.showwarning(message="Enter valid Dose") 
                            flag=False
                            break
                        if validateInt(row[-1])==False:
                            messagebox.showwarning(message="Enter valid Number of Days")
                            flag=False
                            break
                        elif validateDays(row[-1])==False:
                            messagebox.showwarning(message="Enter Number of Days less than 30")
                            flag=False
                            break
                    if validateCb(cbList)==False:
                        messagebox.showwarning(message="Select Time Of Day")
                        flag=False
                        break
            return flag
        # insert data into the table in bulk mode
        if validate2()==True:
            # saving user input data to PatientDetails table
            try:
                ppConn=DBOperations.openDbConnection()
                ppCursor=ppConn.cursor()
                patientPrescInsertQuery=("""INSERT INTO PatientPresc(MobileNumber,Category,MedicineName,Dosage,Unit,Morning,Afternoon,Evening,Night,NoOfDays,TotalQty,DateOfPurchase) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,sysdate())""")
                ppList=[]
                for i in range(len(nlist)):
                    if nlist[i][0]!='':
                        qty=(nlist[i][4]+nlist[i][5]+nlist[i][6]+nlist[i][7])*int(nlist[i][8])
                        nlist[i][2]=int(nlist[i][2])
                        nlist[i][-1]=int(nlist[i][-1])
                        nlist[i].append(qty) 
                        nlist[i].insert(0,int(mobile))
                        ppList.append(nlist[i])
                        # update quantity in meds_db based on the prescription medicine quantity
                        ppCursor.execute("UPDATE meds_db SET Quantity = Quantity-"+str(qty)+ " WHERE medicinename = '"+nlist[i][2]+"'")
                ppCursor.executemany(patientPrescInsertQuery,ppList)
                ppConn.commit()
        
                DBOperations.closeDbConnection(ppConn)
            except mysql.connector.Error as sqlerror:
                print("DB error {}".format(sqlerror))  
            Presc.destroy()   
            messagebox.showinfo(message="Thank you for placing the order!")
           
    prescfrm=Frame(Presc)
    submitBtn1=Button(prescfrm,text="Submit",bg="turquoise",command=click_presc_submit)
    cancelBtn1=Button(prescfrm,text="Cancel",bg="turquoise",command=Presc.destroy)
    cancelBtn1.pack(side=LEFT)
    submitBtn1.pack(side=LEFT)
    prescfrm.grid(row=12,column=2)

    Presc.mainloop()