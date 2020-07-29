#importing libraries
import sqlite3
import re
import datetime

#getting dynamic time and date
now = datetime.datetime.now()
dt = now.strftime("%d/%m/%Y at %H:%M")

#initialising product_info class
class product_info:
    
    mrp = 0
    pur_rate = 0
    sale_rate = 0
    exp_date = " "
    discount = 0.0
    final_price = 0.0

#creating purchase class
class purchase(product_info):
    
#initiaising init method    
    def __init__(self):
        
        print("Inside Purchse")
        com_name = " "
        product_name = " "
   
#creating function for company   
    def input_company(self):
    #declaring names of companies
        print('''+++MENU+++                             
        MENU:-PLEASE SELECT THE COMPANY                  
        1)AGAPPE
        2)BIOMEURIEX
        3)ARKRAY
        4)NIHON KOHDEN
        5)BIOLAB''')
        self.com_name = input()                         #taking input for company

#creating fucntion for product
    def input_product(self):
        
        if(self.com_name == "AGAPPE"):                  #first company and list of products
            print('''PRODUCTS:-
            1)BIO-CHEMISTRY
            2)CELL-COUNTER
            3)MISPA NANO
            4)MISPA NEO
            ''')
        
        elif(self.com_name == "BIOMEURIX"):             #second company and list of products
            print('''PRODUCTS:-
            1)MINI VIDAS
            2)VIDAS
            ''')

        elif(self.com_name == "ARKRAY"):                #third company and list of products
            print('''PRODUCTS:-
            1)PPD 10TU
            2)PPD 2TU
            3)PPD 5TU
            ''')     

        elif(self.com_name == "NIHON KOHDEN"):          #fourth company and list of products
            print('''PRODUCTS:-
            1)CELL COUNTER 3
            2)CELL COUNTER 5
            3)REAGENTS
            ''')

        elif(self.com_name == "BIOLAB"):                #fifth company and list of products
            print('''PRODUCTS:-
            1)GIMSA STAIN
            2)RAPID PAP
            3)LIQUID SOLUTION
            ''')  
        
        self.product_name=input()                       #taking input for product name

#creating function for products information    
    def products(self):
        
        print("\nPLEASE ENTER THE PRODUCT INFORMATION")
        
        print("MRP")
        self.mrp = input()                             #taking product MRP
        
        print("PURCHASE_RATE")                         
        self.pur_rate = input()                        #taking product purchase rate
        
        print("EXPIRY DATE")
        self.exp_date = input()                        #taking product expiry date
        
#creating function for database
    def update_purchase_database(self):
        
        connection_purchase = sqlite3.connect("PROJECT.db")                     #creating connection with database name
        cursor_purchase = connection_purchase.cursor()                          #creating cursor
    #creating table
        cursor_purchase.execute('''CREATE TABLE IF NOT EXISTS purchase( 
                        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,  
                        companyname VARCHAR(30) NOT NULL,
                        productname VARCHAR(30) NOT NULL,  
                        mrp REAL,
                        purchaserate REAL,
                        expdate REAL NOT NULL,
                        date_time REAL NOT NULL
                    ) 
            ''')
        cursor_purchase.execute("INSERT INTO purchase (companyname, productname, mrp, purchaserate, expdate, date_time) VALUES (?, ?, ?, ?, ?, ?)" ,( self.com_name, self.product_name , self.mrp, self.pur_rate, self.exp_date, dt)) 
        
        connection_purchase.commit()                    #saving database 
        connection_purchase.close()                     #closing database
