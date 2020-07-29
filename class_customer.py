#importing libraries
import sqlite3
import re
import datetime

#getting dynamic time and date 
now = datetime.datetime.now()
dt = now.strftime("%d/%m/%Y at %H:%M")

#creating class customer
class customer:
    
    customer_name = " "
    contact_number = " "
    gstno = " "
    email = " "
    address = " "

#creating function for customer details    
    def customer_detail_input(self):
        
        print("PLEASE ENTER THE NAME OF THE CUSTOMER")
        self.customer_name = input()                                #taking input for name
        
        print("PLEASE ENTER THE CONTACT NUMBER OF THE CUSTOMER")
        self.customer_number = int(input())                         #taking input for number
        
        print("PLEASE ENTER THE GST.NO OF THE CUSTOMER")
        self.gstno = input()                                        #taking input for gst number
       
        print("PLEASE ENTER EMAIL OF THE CUSTOMER")
        self.email = input()                                        #taking input for email

        print("PLEASE ENTER THE ADDRESS OF THE CUSTOMER")
        self.address = input()                                      #taking input for address
        
#creating function for database        
    def database_customer(self):
        
        connection_customer = sqlite3.connect("PROJECT.db")         #creating connection with the database name
        cursor_customer = connection_customer.cursor()              #creating cursor
    #creating table
        cursor_customer.execute('''CREATE TABLE IF NOT EXISTS customer(
                        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        customer_name TEXT NOT NULL,
                        customer_number INT NOT NULL,
                        customer_gst_number INT NOT NULL,
                        customer_email TEXT NOT NULL,
                        customer_address TEXT NOT NULL,
                        date_time REAL NOT NULL
                    )'''
        )
        cursor_customer.execute('SELECT customer_gst_number FROM customer WHERE customer_gst_number = {} '.format(self.gstno))
        if cursor_customer.fetchone():
            print("Customer with gstno {} already exists".format(self.gstno))
        else:
            cursor_customer.execute('''INSERT INTO customer(customer_name, customer_number, customer_gst_number, customer_email, customer_address, date_time) VALUES(?, ?, ?, ?, ?, ?)''',
                               (self.customer_name, self.customer_number, self.gstno, self.email, self.address, dt))

        connection_customer.commit()                                #saving database
        connection_customer.close()                                 #closing database

#customerobj = customer()
#customerobj.customer_detail_input()
#customerobj.database_customer()