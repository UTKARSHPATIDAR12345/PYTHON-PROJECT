#importing libraries
import sqlite3
import datetime

#getting dynamic time and date
now = datetime.datetime.now()
dt = now.strftime("%d/%m/%Y at %H:%M")

#initialising product_info class
class product_info:
    
    mrp = 0
    pur_rate = 0
    exp_date = " "
    discount = 0.0
    final_price = 0.0

#creating sales class
class sales(product_info):
    
#initialising init method    
    def __init__(self):
        
        print("Inside sales")
        self.com_name = " "
        self.product_name = " "
        self.customer_name = " "

#creating function for compamy
    def input_company(self):
    #declaring names of companies    
        print('''+++MENU+++
        MENU:-PLEASE SELECT THE COMPANY 
        1)AGAPPE
        2)BIOMEURIEX
        3)ARKRAY
        4)NIHON KOHDEN
        5)BIOLAB''')
        self.com_name = input()                                #taking input for company
        #print(self.com_name)

    def input_product(self):

        if(self.com_name == "AGAPPE"):                         #first company name and list of products
            print('''PRODUCTS:-
            1)BIO-CHEMISTRY
            2)CELL-COUNTER
            3)MISPA NANO
            4)MISPA NEO
            ''')

        elif(self.com_name == "BIOMEURIEX"):                   #second company name and list of products
            print('''PRODUCTS:-
            1)MINI VIDAS
            2)VIDAS
            ''')

        elif(self.com_name == "ARKRAY"):                       #third company name and list of products
            print('''PRODUCTS:-
            1)PPD 10TU
            2)PPD 2TU
            3)PPD 5TU
            ''')     

        elif(self.com_name == "NIHON KOHDEN"):                 #fourth company name and list of products
            print('''PRODUCTS:-
            1)CELL COUNTER 3
            2)CELL COUNTER 5
            3)REAGENTS
            ''')  

        elif(self.com_name == "BIOLAB"):                       #fifth company name and list of products
            print('''PRODUCTS:-
            1)GIMSA STAIN
            2)RAPID PAP
            3)LIQUID SOLUTION
            ''')  
        self.product_name = input()                            #taking input for product name

#initialising function for customer    
    def input_customer(self):
        
        print("\nPLEASE ENTER THE CUSTOMER NAME")
        self.customer_name = input()                           #taking input for customer name

#creating fucntion for products details
    def products(self):
        
        print("\nPLEASE ENTER THE PRODUCT INFORMATION")
        print("MRP")
        self.mrp = input()                                     #taking input for MRP
        
        print("PURCHASE_RATE")
        self.pur_rate = input()                                #taking input for purchase rate
        
        print("EXPIRY DATE")
        self.exp_date = input()                                #taking input for expiry date
        
        print("DISCOUNT")
        self.discount = input()                                #taking input for discount
        
        print("FINAL PRICE")
        self.final_price = input()                             #taking input for final rate

#creating fucntion for database
    def update_database(self):
        
        connection_sale = sqlite3.connect("PROJECT.db")        #creating connection with database name
        cursor_sale = connection_sale.cursor()                 #creating cursor
    #creating database table    
        cursor_sale.execute('''CREATE TABLE IF NOT EXISTS sale(   
                    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    customername VARCHAR(30) NOT NULL,
                    companyname VARCHAR(30) NOT NULL,
                    productname VARCHAR(30) NOT NULL,  
                    mrp REAL,
                    purchaserate REAL,
                    expdate REAL NOT NULL,
                    discount REAL,
                    finalrate REAL,
                    date_time REAL NOT NULL
                ) 
            ''')
        cursor_sale.execute("INSERT INTO sale (customername, companyname, productname, mrp, purchaserate, expdate, discount, finalrate, date_time) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)" ,(self.customer_name, self.com_name, self.product_name , self.mrp, self.pur_rate, self.exp_date, self.discount, self.final_price, dt)) 
        
        connection_sale.commit()                               #saving database
        connection_sale.close()                                #closing database