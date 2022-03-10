from tkinter import *
from time import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font
from turtle import color, exitonclick, ht, left
from Common import *
import DBOperations 
from Prescription import *
from PieChart import *

# Drug Dispensing is the main Window  for the application---
drugDispensingWindow=Tk()
drugDispensingWindow.title("VMS PHARMACEUTICALS")
drugDispensingWindow.grab_set()
drugDispensingWindow.geometry('800x600')
drugDispensingWindow.configure(bg="lightgreen")
# call fucntion to center the window 
centerwindow(drugDispensingWindow,800,600)
# protect the window from maximizing 
drugDispensingWindow.resizable(0,0)

# inner title
lbl=Label(drugDispensingWindow,text="Medicine Order Processing",height=6,bg="lightgreen")
lbl.pack()
vmsfont=tkinter.font.Font(family="Times New Roman",size=10,weight="bold")
lbl.configure(font=vmsfont)

# function to handle clicked event of the pie chart button
def click_chart():
    pieChartWindow=Toplevel(drugDispensingWindow)
    pieChartWindow.grab_set()
    pieChartWindow.title("INVENTORY GRAPH")
    pieChartWindow.geometry("400x50")
    pieChartWindow.configure(bg="lightgreen")
    centerwindow(pieChartWindow,400,50)
    pieChartWindow.resizable(0,0)
    pieChartWindow.lift()

    pieChartFrame = Frame(pieChartWindow)
    selCategory=Label(pieChartWindow,text="Select Category for Chart",bg="lightgreen")
    selCategory.grid(row=1,column=0)

    # get the medicine quantity by category from database
    cat_values=getCategoryValues()

    category1=ttk.Combobox(pieChartWindow,values=cat_values,width=10,state="readonly")
    category1.grid(row=1,column=1)

    # function to handle the clicked event of the submit button on the pie chart window
    def callChart():
        plotMedicineChart(category1.get())

    # function to handle the clicked event of the overall chart button on the pie chart window
    def callOverallChart():
        plotCategoryChart()

    chartBtn=Button(pieChartFrame,text="Submit",bg="turquoise", command=callChart)
    chartBtn.pack(side=LEFT)
    pieCancelBtn=Button(pieChartFrame,text="Cancel",bg="turquoise",command=pieChartWindow.destroy)
    pieCancelBtn.pack(side=LEFT)

    OverallchartBtn=Button(pieChartFrame,text="Overall Chart",bg="turquoise", command=callOverallChart)
    OverallchartBtn.pack(side=LEFT)
    pieChartFrame.grid(row=1,column=3)

    pieChartWindow.mainloop()

# function to handle the clicked event of the new button on the main window
def click_new():
    newButton.configure(activebackground="skyblue")

    # paint the patient registration window
    drugRegistrationWindow=Toplevel(drugDispensingWindow)
    drugRegistrationWindow.grab_set()
    drugRegistrationWindow.title("PATIENT REGISTRATION")
    drugRegistrationWindow.geometry("300x250")
    drugRegistrationWindow.configure(bg="lightgreen")
    centerwindow(drugRegistrationWindow,300,250)
    drugRegistrationWindow.resizable(0,0)

    # function to convert the input value into upper case 
    # characters on key press event
    def upperCaseFName(event):
        v1.set(v1.get().upper())

    # patient fisrt name entry
    firstname=Label(drugRegistrationWindow,text="First Name:",bg="lightgreen")
    v1=StringVar()
    firstname1=Entry(drugRegistrationWindow,textvariable=v1)
    firstname1.bind("<KeyRelease>",upperCaseFName)
    firstname.grid(row=0,column=0)
    firstname1.grid(row=0,column=1)
    firstname1.focus()
    
    def upperCaseLName(event):
        v2.set(v2.get().upper())

    # patient last name entry
    lastname=Label(drugRegistrationWindow,text="Last Name:",bg="lightgreen",anchor="e",justify=LEFT)
    v2=StringVar()
    lastname1=Entry(drugRegistrationWindow,textvariable=v2)
    lastname1.bind("<KeyRelease>",upperCaseLName)
    lastname.grid(row=1,column=0)
    lastname1.grid(row=1,column=1)
    
    # mobile number entry
    name_lbl2=Label(drugRegistrationWindow,text="Mobile Number:",bg="lightgreen",justify='left')
    mobile1=Entry(drugRegistrationWindow, validate="key",validatecommand=(drugRegistrationWindow.register(validate),'%P'))
    name_lbl2.grid(row=2,column=0)
    mobile1.grid(row=2,column=1)

    # select gender radiobutton
    name_lbl=Label(drugRegistrationWindow,text="Gender:",bg="lightgreen")
    frm0=Frame(drugRegistrationWindow)
    gender1=IntVar()

    rb1=Radiobutton(frm0,text="M",variable=gender1,value=1,bg="lightgreen")
    rb2=Radiobutton(frm0,text="F",variable=gender1,value=2,bg="lightgreen")
    rb3=Radiobutton(frm0,text="Other",variable=gender1,value=3,bg="lightgreen")

    rb1.pack(side=LEFT)
    rb2.pack(side=LEFT)
    rb3.pack(side=LEFT)
    name_lbl.grid(row=3,column=0)
    frm0.grid(row=3,column=1)

    # select DOB spinbox
    name_lbl3=Label(drugRegistrationWindow,text="Date Of Birth:",bg="lightgreen")
    frm1=Frame(drugRegistrationWindow)
    sp1=Spinbox(frm1,from_=1,to=31,width=3)
    sp1.pack(side=LEFT)
    months=("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
    
    sp2=Spinbox(frm1,values=months,width=5)
    sp2.pack(side=LEFT)
    year1=Entry(master=frm1,width=7,validate="key",validatecommand=(drugRegistrationWindow.register(validate_year),'%P'))
    year1.pack(side=LEFT)
    name_lbl3.grid(row=4,column=0)
    frm1.grid(row=4,column=1)

    def upperCaseAddress(event):
        v3.set(v3.get().upper())
        
    # address entry 
    name_lbl4=Label(drugRegistrationWindow,text="Address:",bg="lightgreen")
    v3=StringVar()
    address1=Entry(drugRegistrationWindow,textvariable=v3)
    address1.bind("<KeyRelease>",upperCaseAddress)
    name_lbl4.grid(row=5,column=0)
    address1.grid(row=5,column=1)

    def upperCaseAllergies(event):
        v4.set(v4.get().upper())

    # allergies entry
    name_lbl5=Label(drugRegistrationWindow,text="Allergies (if any):",bg="lightgreen")
    v4=StringVar()
    allergies1=Entry(drugRegistrationWindow,textvariable=v4)
    allergies1.bind("<KeyRelease>",upperCaseAllergies)
    name_lbl5.grid(row=6,column=0)
    allergies1.grid(row=6,column=1)

    def upperCaseDoctor(event):
        v5.set(v5.get().upper())

    # doctor ref entry
    name_lbl6=Label(drugRegistrationWindow,text="Doctor Reference:",bg="lightgreen")
    v5=StringVar()
    doctor1=Entry(drugRegistrationWindow,textvariable=v5)
    doctor1.bind("<KeyRelease>",upperCaseDoctor)
    name_lbl6.grid(row=7,column=0)
    doctor1.grid(row=7,column=1) 
    
    # funciton to handle the clicked event of the submit button in patient registration window
    def click_submit():

        fname=firstname1.get()
        lname=lastname1.get()
        mobile=mobile1.get()
        gender=gender1.get()
        month=sp2.get()
        date=sp1.get()
        year=year1.get()
        address=address1.get()
        allergies=allergies1.get()
        doctor=doctor1.get()
        
        # Validate user input data---
        def validation1():
            flag=True
            if refill_validate(mobile)==True:
                messagebox.showwarning(message="Mobile Number already exists")
                flag=False
            if validateNull(fname)==False:
                messagebox.showwarning(message="Please enter the First Name")
                firstname1.configure(background='yellow')
                flag=False
            else:
                firstname1.configure(background='white')
            if validateNull(lname)==False:
                messagebox.showwarning(message="Please enter the Last Name")
                lastname1.configure(background='yellow')
                flag=False
            else:
                lastname1.configure(background='white')
            if validateMobile(mobile)==False:
                messagebox.showwarning(message="Please enter valid Mobile Number")
                mobile1.configure(background='yellow')
                flag=False
            else:
                mobile1.configure(background='white')
            if validateDOByear(year)==False:
                messagebox.showwarning(message="Please enter valid Year of Birth")
                year1.configure(background='yellow')
                flag=False
            else:
                year1.configure(background='white')
            if validateNull(gender)==False:
                messagebox.showwarning(message="Please enter the Gender")
                flag=False
            if validateNull(address)==False:
                messagebox.showwarning(message="Please enter the Address")
                address1.configure(background='yellow')
                flag=False
            else:
                address1.configure(background='white')
            if validateNull(doctor)==False:
                messagebox.showwarning(message="Please enter the Doctor Reference Details")
                doctor1.configure(background='yellow')
                flag=False
            else:
                doctor1.configure(background='white')
            return flag    
        
        if validation1()==True:

            # Saving user input data to PatientDetails table upon successful validation
            pdConn=DBOperations.openDbConnection()
            pdCursor=pdConn.cursor()
            patientInsertQuery=("INSERT INTO PatientDetails (MobileNumber, FirstName, LastName, Gender, DOB, Address, Allergies, Doctor, RegistrationDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,curdate())")
            if gender==1:
                genderEntry='M'
            elif gender==2:
                genderEntry='F'
            else:
                genderEntry='O'
            DOBdate=date+'-'+month+'-'+year
            pdList=[int(mobile),fname,lname,genderEntry,DOBdate,address,allergies,doctor]
            pdCursor.execute(patientInsertQuery,pdList)
            pdConn.commit()
            DBOperations.closeDbConnection(pdConn)

            drugRegistrationWindow.destroy()

            openPrescription("NEW",drugDispensingWindow,mobile)
    
            
    frm2=Frame(drugRegistrationWindow)
    submitBtn=Button(frm2,text="Submit",bg="turquoise",command=click_submit)
    cancelBtn=Button(frm2,text="Cancel",bg="turquoise",command=drugRegistrationWindow.destroy)
    cancelBtn.pack(side=LEFT)
    submitBtn.pack(side=LEFT)
    frm2.grid(row=8,column=1)

    drugRegistrationWindow.mainloop()

# function to handle the clicked event of the refill button on the main window 
def click_refill():
    refillButton.configure(activebackground="skyblue")
    refWindow=Toplevel(drugDispensingWindow)
    refWindow.grab_set()
    refWindow.title("PRESCRIPTION REFILL")
    refWindow.configure(bg="lightgreen")
    refWindow.geometry("300x250")
    refWindow.resizable(0,0)
    centerwindow(refWindow,300,250)

    # search mobile number
    search_lbl=Label(refWindow,text="Enter Mobile Number:",bg="lightgreen")
    mobilenumber=Entry(refWindow, validate="key",validatecommand=(refWindow.register(validate),'%P'))
    search_lbl.grid(row=0,column=0)
    mobilenumber.grid(row=0,column=1)
    mobilenumber.focus()

    # validation for mobile search 
    def refillCommand():
        num=mobilenumber.get()
        
        MobileNull = False
        refillFlag = False
        # validation of mobile number
        MobileNull=validateNull(num)
        if MobileNull==False:      
            messagebox.showwarning(message="Please enter Mobile Number")
            refWindow.lift()
        else:
            refillFlag=refill_validate(num)
        
        if refillFlag==True:
            refWindow.destroy()
            # retrieve prescription data from database for the given mobile number in REFILL mode
            openPrescription("REFILL",drugDispensingWindow,num)
        elif MobileNull==True and refillFlag==False:
            messagebox.showinfo(message="Mobile Number not found")

    searchButton=Button(refWindow,text="Search",command=refillCommand,bg="turquoise")
    searchButton.grid(row=0,column=2)
    
    refWindow.mainloop()

# function to handle the clicked evenr of inventory button in the main window 
def click_inv():
    inventoryButton.configure(activebackground="skyblue")
    InvWindow=Toplevel(drugDispensingWindow)
    InvWindow.grab_set()
    InvWindow.title("MEDICINE INVENTORY")
    InvWindow.configure(bg="lightgreen")
    InvWindow.resizable(0,0)
    centerwindow(InvWindow,800,500)

    # display the medicine inventory details in a treeview control
    class Table:
        def __init__(self,InvWindow):

            inframe=Frame(InvWindow,width=800,height=500)
            inframe.pack()

            style=ttk.Style().configure("Treeview", rowheight=30, background="lightgreen", foreground="black")
            style1=ttk.Style().configure("Treeview.Heading", background="blue", foreground="black")
            inventory = ttk.Treeview(inframe,selectmode="extended",height=500)
            inventory.place(x=5,y=30)   

            # treeview columns
            inventory['columns'] = ('med_num', 'category', 'medicine_name', 'type', 'quantity','information')

            inventory.column('#0', width=0, stretch=NO, anchor=W)
            inventory.column("med_num", width=40, anchor=W)
            inventory.column("category",width=80, anchor=W)
            inventory.column("medicine_name",width=100, anchor=W)
            inventory.column("type",width=80, anchor=W)
            inventory.column("quantity",width=60, anchor=W)
            inventory.column("information",width=500, anchor=W)
            
            # treeview header labels
            inventory.heading('#0', text='', anchor=W)
            inventory.heading("med_num",text="S.No", anchor=W)
            inventory.heading("category",text="Category", anchor=W)
            inventory.heading("medicine_name",text="Medicine Name", anchor=W)
            inventory.heading("type",text="Type", anchor=W)
            inventory.heading("quantity",text="Quantity", anchor=W)
            inventory.heading("information",text="Description", anchor=W)

            for i in range(total_rows):
                inventory.insert(parent='',index='end',iid=i,text='', values=(lis[i]))
            inventory.pack()
                    
    invConn=DBOperations.openDbConnection()
    invCursor=invConn.cursor()
    invQuery=("SELECT * from meds_db")
    invCursor.execute(invQuery)
    lis=invCursor.fetchall()
    total_rows = len(lis)
    tabledisp=Table(InvWindow)

    DBOperations.closeDbConnection(invConn)
    
    InvWindow.mainloop()

# function to handle the clicked event of patient details button in the main window
def click_pdts():
    patientDetailsButton.configure(activebackground="skyblue")
    PdtsWindow=Toplevel(drugDispensingWindow)
    PdtsWindow.grab_set()
    PdtsWindow.title("PATIENT DETAILS")
    PdtsWindow.geometry("300x250")
    PdtsWindow.configure(bg="lightgreen")
    PdtsWindow.resizable(0,0)
    centerwindow(PdtsWindow,300,250)

    # search by mobile number
    search_label1=Label(PdtsWindow,text="Enter Mobile Number:",bg="lightgreen")
    mobilenumber1=Entry(PdtsWindow, validate="key",validatecommand=(PdtsWindow.register(validate),'%P'))
    search_label1.grid(row=0,column=0)
    mobilenumber1.grid(row=0,column=1)
    mobilenumber1.focus()

    # validation of mobile number
    def PdtsCommand():
        
        PdWindow=Toplevel(PdtsWindow)
        PdWindow.grab_set()
        PdWindow.geometry("800x400")
        PdWindow.resizable(0,0)
        PdWindow.configure(bg="lightgreen")
        centerwindow(PdWindow, 800,400)

        mob_num=mobilenumber1.get()
        MobileNull = False
        refillFlag = False

        MobileNull=validateNull(mob_num)
        if MobileNull==False:
            PdWindow.destroy()
            messagebox.showwarning(message="Please enter Mobile Number")
            PdtsWindow.lift()
        else:
            refillFlag = refill_validate(mob_num)
        
        # display patient details from database based on the mobile number 
        if refillFlag==True:
            PdtsConn=DBOperations.openDbConnection()
            PdtsCursor=PdtsConn.cursor()
            # window title with the patient name and mobile number
            PdtsQuery="SELECT concat('Name: ',firstname,' ',lastname, ' Mobile: ', mobilenumber) FROM PatientDetails where MobileNumber ="+mob_num
            PdtsCursor.execute(PdtsQuery)
            PdtsList=PdtsCursor.fetchall()
            PdWindow.title(PdtsList[0])
            # patient details 
            PurchQuery="SELECT PrescId, Category, MedicineName, Dosage, Unit, Totalqty, DateOfPurchase FROM patientpresc where MobileNumber="+mob_num
            PdtsCursor.execute(PurchQuery)
            PurchList=PdtsCursor.fetchall()

            list2=["Presc Id","Category","Medicine Name","Dosage","Unit","Total Quantity", "Purchase Date"]
            PurchList.insert(0,list2)

            # creation of patient details table
            class Table1:
                def __init__(self,PdWindow):
                    pdframe=Frame(PdWindow)
                    total_rows=len(PurchList)
                    total_columns=len(PurchList[0])
                    for i in range(total_rows):
                        for j in range(total_columns):
                            self.e = Text(pdframe, fg='black',bg="lightgreen", width=18, font=('Times New Roman',10),height=1)
                            self.e.grid(row=i, column=j)
                            self.e.insert(END,PurchList[i][j])
                            self.e.configure(state='disabled')
                            if i==0:
                                self.e.configure(bg="green")
                            pdframe.pack()
                    
            pdtabledisp=Table1(PdWindow)
            DBOperations.closeDbConnection(PdtsConn)
            
            PdWindow.mainloop()

        elif MobileNull==True and refillFlag==False:
            PdWindow.destroy()
            messagebox.showwarning(message="Mobile Number not found")

    searchButton=Button(PdtsWindow,text="Search",command=PdtsCommand)
    searchButton.grid(row=0,column=2)

    PdtsWindow.mainloop()

# main window controls 
frm1=Frame(master=drugDispensingWindow)
newButton=Button(frm1,text="New",bg="turquoise",command=click_new,height=2,width=10)
newButton.pack(side=LEFT)
refillButton=Button(frm1,text="Refill",bg="turquoise",command=click_refill,height=2,width=10)
refillButton.pack()
frm1.pack()
patientDetailsButton=Button(drugDispensingWindow,text="Patient Details",command=click_pdts,height=2,width=21)
patientDetailsButton.pack()
inventoryButton=Button(drugDispensingWindow,text="Inventory",command=click_inv,height=2,width=21)
inventoryButton.pack()
PieChartButton=Button(drugDispensingWindow,text="Pie Chart",height=2,width=21,command=click_chart)
PieChartButton.pack()

drugDispensingWindow.mainloop()