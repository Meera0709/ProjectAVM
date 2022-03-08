import mysql.connector
import csv

#This is standalone program to create the database tables for the project

#---Complete list of Medicines---

medlist=[[1,"ENT","Astrepo","Nasal Spray",1000,"Azelastine Hydrochloride Nasal Spray"],
[2,"ENT","Caprelsa","Tablets",1000,"vandetanib"],
[3,"ENT","Dymista","Nasal Spray",1000,"azelastine hydrochloride and fluticasone propionate"],
[4,"ENT","Erbitux","Fluid",1000,"Azelastine Hydrochloride Nasal Spray"],
[5,"ENT","Grastek","Tablets",1000,"Cetuxinab"],
[6,"ENT","Keytruda","Fluid",1000,"Timothy Grass Pollen Allergen Extract"],
[7,"ENT","Lenvima","Tablets",1000,"lenvatinib"],
[8,"ENT","Nucala","Fluid",1000,"mepolizumab"],
[9,"ENT","Oralair","Extract",1000,"""Sweet Vernal, Orchard, Perennial Rye,
Timothy and Kentucky Blue Grass Mixed Pollens Allergen Extract"""],
[10,"ENT","Oravig","Tablets",1000,"Miconazole"],
[11,"ENT","Otiprio","Fluid",1000,"ciprofloxacin otic suspension"],
[12,"ENT","Patanase","Nasal Spray",1000,"olopatadine hydrochloride"],
[13,"ENT","Protonix","Tablets",1000,"pantoprazole sodium"],
[14,"ENT","Qnasl","Nasal Spray",1000,"beclomethasone dipropionate"],
[15,"ENT","Ragwitek","Extract",1000,"Short Ragweed Pollen Allergen Extract"],
[16,"ENT","Salagen","Tablets",1000,"pilocarpine hydrochloride"],
[17,"ENT","Xolair","Nasal Spray",1000,"omalizunub"],
[18,"ENT","Xtoro","Suspension",1000,"finafloxacin otic suspension"],
[19,"ENT","Xyzal","Syrup",1000,"levocetirizine dihydrochloride"],
[20,"ENT","Zithromax","Tablets",1000,"azithromycin"],


[21,"Ophthalmic","Vigamox","Eyedrop",1000,"moxifloxacin"],
[22,"Ophthalmic","Zymar","Eyedrop",1000,"gatifloxacin"],
[23,"Ophthalmic","Vigamox","Eyedrop",1000,"moxifloxacin"],
[24,"Ophthalmic","Zirgan","Eyedrop",1000,"ganciclovir"],
[25,"Ophthalmic","Azasite","Eyedrop",1000,"azithromycin"],
[26,"Ophthalmic","Polytrim","Eyedrop",1000," polymyxin b / trimethoprim"],
[27,"Ophthalmic","Moxeza","Eyedrop",1000,"moxifloxacin"],
[28,"Ophthalmic","Besivance","Eyedrop",1000,"besifloxacin"],
[29,"Ophthalmic","Tobrex","Eyedrop",1000,"tobramycin"],
[30,"Ophthalmic","Zymaxid","Eyedrop",1000,"gatifloxacin"],
[31,"Ophthalmic","Vitrasert ","Eyedrop",1000,"ganciclovir"],
[32,"Ophthalmic","Viroptic","Eyedrop",1000,"trifluridine"],
[33,"Ophthalmic","Natacyn","Eyedrop",1000,"natamycin"],
[34,"Ophthalmic","Iquix","Eyedrop",1000,"levofloxacin"],
[35,"Ophthalmic","Ciloxan","Eyedrop",1000,"ciprofloxacin"],
[36,"Ophthalmic","Baciguent","Eyedrop",1000,"bacitracin"],
[37,"Ophthalmic","Vira-A","Eyedrop",1000,"vidarabine"],
[38,"Ophthalmic","Tomycine","Eyedrop",1000,"tobramycin"],
[39,"Ophthalmic","Tobrasol","Eyedrop",1000,"tobramycin"],
[40,"Ophthalmic","Sulf-10","Eyedrop",1000,"sulfacetamide sodium"],
[41,"Ophthalmic","Terramycin with Polymyxin B Sulfate","Eyedrop",1000,"oxytetracycline / polymyxin b"],
[42,"Ophthalmic","Roymicin","Eyedrop",1000,"erythromycin"],
[43,"Ophthalmic","Quixin","Eyedrop",1000,"levofloxacin"],
[44,"Ophthalmic","Ocuflox","Eyedrop",1000,"ofloxacin"],
[45,"Ophthalmic","Ocu-Mycin","Eyedrop",1000,"gentamicin"],
[46,"Ophthalmic","Ocu-Chlor","Eyedrop",1000,"chloramphenicol"],
[47,"Ophthalmic","Neosporin Ophthalmic ","Eyedrop",1000,"gramicidin / neomycin / polymyxin b"],
[48,"Ophthalmic","Neocidin Ophthalmic Solution","Eyedrop",1000,"gramicidin / neomycin / polymyxin b"],
[49,"Ophthalmic","Neo-Polycin","Eyedrop",1000,"bacitracin / neomycin / polymyxin b"],
[50,"Ophthalmic","Isopto Cetamide","Eyedrop",1000,"sulfacetamide sodium"],
[51,"Ophthalmic","Ilotycin","Eyedrop",1000,"erythromycin"],
[52,"Ophthalmic","Gentasol","Eyedrop",1000,"gentamicin"],
[53,"Ophthalmic","Gentak","Eyedrop",1000,"gentamicin"],
[54,"Ophthalmic","Gentacidin","Eyedrop",1000,"gentamicin"],
[55,"Ophthalmic","Genoptic","Eyedrop",1000,"gentamicin"],
[56,"Ophthalmic","Garamycin Ophthalmic","Eyedrop",1000,"gentamicin"], 
[57,"Ophthalmic","Genoptic","Eyedrop",1000,"gentamicin"],
[58,"Ophthalmic","Eyemycin","Eyedrop",1000,"erythromycin"],
[59,"Ophthalmic","Dendrid","Eyedrop",1000,"idoxuridine"],
[60,"Ophthalmic","Chloroptic","Eyedrop",1000,"chloramphenicol"],
[61,"Ophthalmic","Chloromycetin Ophthalmic","Eyedrop",1000,"chloramphenicol"],
[62,"Ophthalmic","Bleph-10","Eyedrop",1000,"sulfacetamide sodium"],
[63,"Ophthalmic","Betadine Ophthalmic Solution","Eyedrop",1000,"povidone iodine"],
[64,"Ophthalmic","AK-Tob","Eyedrop",1000,"tobramycin"],
[65,"Ophthalmic","AK-Poly-Bac","Eyedrop",1000,"bacitracin / polymyxin b"],
[66,"Ophthalmic","AK-Chlor","Eyedrop",1000,"chloramphenicol"],


[67,"PainKillers","Toradol (Pro)","Tablets",1000,"Ketorolac"],
[68,"PainKillers","Voltaren (Pro)","Tablets",1000,"Diclofenac"],
[69,"PainKillers","Aleve","Tablets",1000,"Naproxen"],
[70,"PainKillers","Mobic (Pro)","Tablets",1000,"Meloxicam"],
[71,"PainKillers","Sprix (Pro)","Nasal Spray",1000,"Ketorolac"],
[72,"PainKillers","Cambia (Pro)","Oral Powder",1000,"Diclofenac"],
[73,"PainKillers","Vimovo (Pro)","Tablets",1000,"esomeprazole / naproxen"],
[74,"PainKillers","Cataflam (Pro)","Tablets",1000,"diclofenac"],
[75,"PainKillers","Arthrotec (Pro)","Tablets",1000,"diclofenac / misoprostol"],
[76,"PainKillers","Duexis (Pro)","Tablets",1000,"famotidine / ibuprofen"],
[77,"PainKillers","Zipsor (Pro)","Tablets",1000,"diclofenac"],
[78,"PainKillers","Advil (Pro)","Tablets",1000,"ibuprofen"],
[79,"PainKillers","Relafen (Pro)","Tablets",1000,"nabumetone"],
[80,"PainKillers","Naprosyn (Pro)","Tablets",1000,"naproxen"],
[81,"PainKillers","Indocin (Pro)","Tablets",1000,"indomethacin"],
[82,"PainKillers","Zorvolex (Pro)","Tablets",1000,"diclofenac"],
[83,"PainKillers","Advil Liqui-Gels (Pro)","Tablets",1000,"ibuprofen"],
[84,"PainKillers","Toradol IV / IM","Tablets",1000,"ketorolac"],
[85,"PainKillers","Ponstel (Pro)","Tablets",1000,"mefenamic acid"],
[86,"PainKillers","Motrin (Pro)","Tablets",1000,"ibuprofen"],
[87,"PainKillers","Naprelan (Pro)","Tablets",1000,"naproxen"],
[88,"PainKillers","Lodine (Pro)","Tablets",1000,"etodolac"],
[89,"PainKillers","Feldene (Pro)","Tablets",1000,"piroxicam"],
[90,"PainKillers","Anaprox","Tablets",1000,"naproxen"],
[91,"PainKillers","Indocin SR (Pro)","Tablets",1000,"indomethacin"],
[92,"PainKillers","Voltaren-XR (Pro)","Tablets",1000,"diclofenac"],
[93,"PainKillers","Motrin IB (Pro)","Tablets",1000,"ibuprofen"],
[94,"PainKillers","Clinoril (Pro)","Tablets",1000,"sulindac"],
[95,"PainKillers","Anaprox-DS","Tablets",1000,"naproxen"],
[96,"PainKillers","Orudis KT","Tablets",1000,"ketoprofen"],
[97,"PainKillers","Dolobid","Tablets",1000,"diflunisal"],
[98,"PainKillers","Daypro (Pro)","Tablets",1000,"oxaprozin"],
[99,"PainKillers","Children's Motrin","Tablets",1000,"ibuprofen"],
[100,"PainKillers","Ansaid (Pro)","Tablets",1000,"flurbiprofen"],

[101,"Diabetes","Tolbutamide ","Tablets",1000,"Orinase®"],
[102,"Diabetes","Glimepiride ","Tablets",1000,"Amaryl®"],
[103,"Diabetes","Glipizide ","Tablets",1000,"Glucotrol®"],
[104,"Diabetes","Glyburide ","Tablets",1000,"Micronase®,DiaBeta®"],
[105,"Diabetes","Glyburide, micronized","Tablets",1000,"Glynase PresTab®"],
[106,"Diabetes","Repaglinide ","Tablets",1000,"Prandin®"],
[107,"Diabetes","Nateglinide ","Tablets",1000,"Starlix®"],
[108,"Diabetes","Metformin","Tablets",1000,"Glucophage®"],
[109,"Diabetes","Acarbose ","Tablets",1000,"Precose®"],
[110,"Diabetes","Pioglitazone","Tablets",1000,"Actos®"],
[111,"Diabetes","Exenatide","Shot",1000,"Byetta®"],
[112,"Diabetes","Liraglutide","Shot",1000,"Victoza®"],
[113,"Diabetes","Albiglutide","Shot",1000,"Tanzeum®"],
[114,"Diabetes","Dulaglutide","Shot",1000,"Trulicity®"],
[115,"Diabetes","Sitagliptin","Tablets",1000,"Onglyza®"],
[116,"Diabetes","Saxagliptin","Tablets",1000,"Tradjenta®"],
[117,"Diabetes","Linagliptin","Tablets",1000,"Januvia®"],
[118,"Diabetes","Canagliflozin","Tablets",1000,"Invokana®"],
[119,"Diabetes","Dapagliflozin","Tablets",1000,"Farxiga®"],
[120,"Diabetes","Empagliflozin","Tablets",1000,"Jardiance®"]]

try:
        #Open the database connection to the project DB
        dbConnection=mysql.connector.connect(host="localhost",user="root",password="0410",database="project")
        cursor=dbConnection.cursor()
        print("DB connection success")

        #---Table creation - Meds_db ---
        query1="""CREATE TABLE IF NOT EXISTS Meds_db
                (Med_Num int Primary Key, 
                Category varchar(50), 
                MedicineName varchar(100), 
                Type varchar(50),
                Quantity int,
                Information varchar(700))"""
        
        cursor.execute(query1)
        print("Table meds_db created successfully")

        #---Table creation - PatientDetails ---
        query2="""CREATE TABLE IF NOT EXISTS PatientDetails
                (MobileNumber bigint Primary Key, 
                FirstName varchar(50),
                LastName varchar(50),
                Gender char(1),
                DOB varchar(12), 
                Address varchar(200),
                Allergies varchar(100),
                Doctor varchar(100),
                RegistrationDate date)"""

        cursor.execute(query2)
        print("Table PatientDetails created successfully")

        #---Table creation - PatientPresc ---
        query3="""CREATE TABLE IF NOT EXISTS PatientPresc
                (PrescId int auto_increment primary key,
                MobileNumber bigint, foreign key(MobileNumber) references PatientDetails(MobileNumber), 
                Category varchar(50),
                MedicineName varchar(50),
                Dosage varchar(10),
                Unit varchar(10), 
                Morning bool,
                Afternoon bool,
                Evening bool,
                Night bool,
                NoOfDays int,
                TotalQty int,
                DateOfPurchase date)"""

        cursor.execute(query3)
        print("Table PatientPresc created successfully")

        #---Table population---
        dbQuery = ("INSERT INTO Meds_db (Med_Num, Category, MedicineName, Type, Quantity, Information) VALUES (%s,%s,%s,%s,%s,%s)")

        cursor.executemany(dbQuery,medlist)
        dbConnection.commit()

        #---update trigger on orderplacement---
        TriggerQuery="""create trigger afterPrescRequest after insert on patientpresc for each row
                        update meds_db A, patientpresc B 
                        set A.Quantity = A.Quantity-B.TotalQty 
                        where A.MedicineName = B.MedicineName;"""
        cursor.execute(TriggerQuery)

        #---CSV file creation to hold the medicine name and category for populating drop down box later ---
        csvSelectQuery="SELECT Category, MedicineName from Meds_db"
        cursor.execute(csvSelectQuery)
        listObj=cursor.fetchall()
        f=open("medicine.csv",'w')
        writer=csv.writer(f)
        writer.writerows(listObj)
        f.close()

        dbConnection.close()

except mysql.connector.Error as sqlerror:
        print("DB error {}".format(sqlerror)) 
