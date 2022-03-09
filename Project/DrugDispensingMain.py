from tkinter import *
from time import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font
from turtle import color, exitonclick
from Common import *
import DbOperations 
from Prescription import *

#---Main Window Creation---
drugDispensingWindow=Tk()
drugDispensingWindow.title("Drug Dispensing")
drugDispensingWindow.grab_set()
drugDispensingWindow.geometry('800x600')
drugDispensingWindow.configure(bg="lightgreen")
centerwindow(drugDispensingWindow,800,600)
drugDispensingWindow.resizable(0,0)

lbl=Label(drugDispensingWindow,text="VMS PHARMACEUTICALS",height=6,bg="lightgreen")
lbl.pack()
vmsfont=tkinter.font.Font(family="Times New Roman",size=10,weight="bold")
lbl.configure(font=vmsfont)

#---new button function---
def click_new():
    newButton.configure(activebackground="skyblue")

    #---opens new window---
    drugRegistrationWindow=Toplevel(drugDispensingWindow)
    drugRegistrationWindow.grab_set()
    drugRegistrationWindow.title("Registration")
    drugRegistrationWindow.geometry("300x250")
    drugRegistrationWindow.configure(bg="lightgreen")
    centerwindow(drugRegistrationWindow,300,250)
    drugRegistrationWindow.resizable(0,0)

    def upperCaseFName(event):
        v1.set(v1.get().upper())

    #---patient fisrt name entry---
    firstname=Label(drugRegistrationWindow,text="First Name:",bg="lightgreen")
    v1=StringVar()
    firstname1=Entry(drugRegistrationWindow,textvariable=v1)
    firstname1.bind("<KeyRelease>",upperCaseFName)
    firstname.grid(row=0,column=0)
    firstname1.grid(row=0,column=1)
    firstname1.focus()
    
    def upperCaseLName(event):
        v2.set(v2.get().upper())

    #---patient last name entry---
    lastname=Label(drugRegistrationWindow,text="Last Name:",bg="lightgreen",anchor="e",justify=LEFT)
    v2=StringVar()
    lastname1=Entry(drugRegistrationWindow,textvariable=v2)
    lastname1.bind("<KeyRelease>",upperCaseLName)
    lastname.grid(row=1,column=0)
    lastname1.grid(row=1,column=1)
    
    #---mobile number entry---
    name_lbl2=Label(drugRegistrationWindow,text="Mobile Number:",bg="lightgreen",justify='left')
    mobile1=Entry(drugRegistrationWindow, validate="key",validatecommand=(drugRegistrationWindow.register(validate),'%P'))
    name_lbl2.grid(row=2,column=0)
    mobile1.grid(row=2,column=1)

    #---select gender radiobutton---
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

    #---select DOB spinbox---
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
        
    #---address entry---
    name_lbl4=Label(drugRegistrationWindow,text="Address:",bg="lightgreen")
    v3=StringVar()
    address1=Entry(drugRegistrationWindow,textvariable=v3)
    address1.bind("<KeyRelease>",upperCaseAddress)
    name_lbl4.grid(row=5,column=0)
    address1.grid(row=5,column=1)

    def upperCaseAllergies(event):
        v4.set(v4.get().upper())

    #---allergies entry---
    name_lbl5=Label(drugRegistrationWindow,text="Allergies (if any):",bg="lightgreen")
    v4=StringVar()
    allergies1=Entry(drugRegistrationWindow,textvariable=v4)
    allergies1.bind("<KeyRelease>",upperCaseAllergies)
    name_lbl5.grid(row=6,column=0)
    allergies1.grid(row=6,column=1)

    def upperCaseDoctor(event):
        v5.set(v5.get().upper())

    #---doctor ref entry---
    name_lbl6=Label(drugRegistrationWindow,text="Doctor Reference:",bg="lightgreen")
    v5=StringVar()
    doctor1=Entry(drugRegistrationWindow,textvariable=v5)
    doctor1.bind("<KeyRelease>",upperCaseDoctor)
    name_lbl6.grid(row=7,column=0)
    doctor1.grid(row=7,column=1) 

    def click_submit():
        print("inside submit")
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
        
        #---Validate user input data---
        def validation1():
            flag=True
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

            #---saving user input data to PatientDetails table---
            pdConn=DbOperations.openDbConnection()
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
            DbOperations.closeDbConnection(pdConn)

            drugRegistrationWindow.destroy()

            openPrescription("NEW",drugDispensingWindow,mobile)
    
            
    #---submit details to close window---
    frm2=Frame(drugRegistrationWindow)
    submitBtn=Button(frm2,text="Submit",bg="turquoise",command=click_submit)
    cancelBtn=Button(frm2,text="Cancel",bg="turquoise",command=drugRegistrationWindow.destroy)
    cancelBtn.pack(side=LEFT)
    submitBtn.pack(side=LEFT)
    frm2.grid(row=8,column=1)
    print("before open")
    drugRegistrationWindow.mainloop()

#---refill button function---
def click_refill():
    refillButton.configure(activebackground="skyblue")
    refWindow=Toplevel(drugDispensingWindow)
    refWindow.grab_set()
    refWindow.title("Refill")
    refWindow.configure(bg="lightgreen")
    refWindow.geometry("300x250")
    refWindow.resizable(0,0)
    centerwindow(refWindow,300,250)


    #---searching mobile number---
    search_lbl=Label(refWindow,text="Enter Mobile Number:",bg="lightgreen")
    mobilenumber=Entry(refWindow, validate="key",validatecommand=(refWindow.register(validate),'%P'))
    search_lbl.grid(row=0,column=0)
    mobilenumber.grid(row=0,column=1)
    mobilenumber.focus()
    def refillCommand():
        num=mobilenumber.get()
        if refill_validate(num):
            openPrescription("REFILL",drugDispensingWindow,num)
            refWindow.destroy()
        else:
            messagebox.showinfo(message="Mobile Number not found")
    searchButton=Button(refWindow,text="Search",command=refillCommand,bg="turquoise")
    searchButton.grid(row=0,column=2)
    
    refWindow.mainloop()

#---inventory button function---
def click_inv():
    inventoryButton.configure(activebackground="skyblue")
    InvWindow=Toplevel(drugDispensingWindow)
    InvWindow.grab_set()
    InvWindow.title("Drug Inventory")
    InvWindow.geometry("800x600")
    InvWindow.configure(bg="lightgreen")
    InvWindow.resizable(0,0)
    centerwindow(InvWindow,800,600)

    class Table:
        def __init__(self,InvWindow):
            global inframe
            inframe=Frame(InvWindow)
            for i in range(total_rows):
                for j in range(total_columns):
                    if j==0 or j==4:
                        self.e = Text(inframe,fg='black', width=5, font=('Times New Roman',8),height=1)
                        self.e.grid(row=i, column=j)
                    elif j==5:
                        self.e = Text(inframe,fg='black',width=200, font=('Times New Roman',8),height=1)
                        self.e.grid(row=i, column=j)
                    else:
                        self.e = Text(inframe,fg='black',width=15, font=('Times New Roman',8),height=1)
                        self.e.grid(row=i, column=j)
                    self.e.insert(END,lis[i][j])
                    self.e.configure(state='disabled')
                    inframe.pack()
    
    invConn=DbOperations.openDbConnection()
    invCursor=invConn.cursor()
    invQuery=("SELECT * from meds_db")
    invCursor.execute(invQuery)
    lis=invCursor.fetchall()
    total_rows = len(lis)
    total_columns = len(lis[0])
    tabledisp=Table(InvWindow)

    canvas=Canvas(inframe)
    scrollbar=Scrollbar(inframe,orient="vertical",command=canvas.yview)
    scrollable_frame=Frame(canvas)
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0),window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    scroll_lbl=Label(scrollable_frame).pack()
    canvas.pack(side=LEFT,fill=BOTH,expand=True)
    scrollbar.pack(side=RIGHT,fill=Y)

    DbOperations.closeDbConnection(invConn)
    
    InvWindow.mainloop()

#---patient details---
def click_pdts():
    patientDetailsButton.configure(activebackground="skyblue")
    PdtsWindow=Toplevel(drugDispensingWindow)
    PdtsWindow.grab_set()
    PdtsWindow.title("Mobile")
    PdtsWindow.geometry("300x250")
    PdtsWindow.configure(bg="lightgreen")
    PdtsWindow.resizable(0,0)
    centerwindow(PdtsWindow,300,250)

    #---searching mobile number---
    search_label1=Label(PdtsWindow,text="Enter Mobile Number:",bg="lightgreen")
    mobilenumber1=Entry(PdtsWindow, validate="key",validatecommand=(PdtsWindow.register(validate),'%P'))
    search_label1.grid(row=0,column=0)
    mobilenumber1.grid(row=0,column=1)
    mobilenumber1.focus()

    def PdtsCommand():
        
        PdWindow=Toplevel(drugDispensingWindow)
        PdWindow.grab_set()
        PdWindow.geometry("800x600")
        PdWindow.resizable(0,0)
        PdWindow.configure(bg="lightgreen")
        centerwindow(PdWindow,800,600)
        mob_num=mobilenumber1.get()
        
        refillFlag = False
        if validateNull(mob_num)==False:
            messagebox.showwarning(message="Please enter Mobile Number")
        else:
            refillFlag = refill_validate(mob_num)
        
        if refillFlag==True:
            PdtsConn=DbOperations.openDbConnection()
            PdtsCursor=PdtsConn.cursor()
            PdtsQuery="SELECT concat('Name: ',firstname,' ',lastname, ' Mobile: ', mobilenumber) FROM PatientDetails where MobileNumber ="+mob_num
            PdtsCursor.execute(PdtsQuery)
            PdtsList=PdtsCursor.fetchall()
            PdWindow.title(PdtsList[0])
            PurchQuery="SELECT PrescId, Category, MedicineName, Dosage, Unit, Totalqty, sysdate() as DateOfPurchase FROM patientpresc where MobileNumber="+mob_num
            PdtsCursor.execute(PurchQuery)
            PurchList=PdtsCursor.fetchall()
           
            list2=["Presc Id","Category","Medicine Name","Dosage","Unit","Total Quantity", "Purchase Date"]
            PurchList.insert(0,list2)
           
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
            DbOperations.closeDbConnection(PdtsConn)
            PdtsWindow.destroy()
            PdWindow.mainloop()
        else:
            messagebox.showwarning(message="Mobile Number not found")

    searchButton=Button(PdtsWindow,text="Search",command=PdtsCommand)
    searchButton.grid(row=0,column=2)

    PdtsWindow.mainloop()

#---homepage buttons---
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
PieChartButton=Button(drugDispensingWindow,text="Pie Chart",height=2,width=21)
PieChartButton.pack()

drugDispensingWindow.mainloop()
