import sqlite3
import re

class customer:
    
    customer_name = " "
    contact_number = " "
    gstno = " "
    email = " "
    address = " "
    customer_debit = 0

    def customer_detail_input(self):
        print("PLEASE ENTER THE NAME OF THE CUSTOMER")
        self.customer_name = input()
        
        print("PLEASE ENTER THE CONTACT NUMBER OF THE CUSTOMER")
        self.customer_number = int(input())
        
        print("PLEASE ENTER THE GST.NO OF THE CUSTOMER")
        self.gstno = input()
       
        print("PLEASE ENTER EMAIL OF THE CUSTOMER")
        self.email = input()

        print("PLEASE ENTER THE ADDRESS OF THE CUSTOMER")
        self.address = input()
        
    def database_customer(self):
        connection_customer = sqlite3.connect("PROJECT.db")
        cursor_customer = connection_customer.cursor()
        cursor_customer.execute('''CREATE TABLE IF NOT EXISTS customer(
                        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        customer_name TEXT,
                        customer_number INT NOT NULL,
                        customer_gst_number INT NOT NULL,
                        customer_email TEXT NOT NULL,
                        customer_address TEXT NOT NULL
                    )'''
        )
        cursor_customer.execute('SELECT customer_gst_number FROM customer WHERE customer_gst_number = {} '.format(self.gstno))
        if cursor_customer.fetchone():
            print("Customer with gstno {} already exists".format(self.gstno))
        else:
            cursor_customer.execute('''INSERT INTO customer(customer_name, customer_number, customer_gst_number, customer_email, customer_address) VALUES(?, ?, ?, ?, ?)''',
                               (self.customer_name, self.customer_number, self.gstno, self.email, self.address))

        connection_customer.commit()
        connection_customer.close()


customerobj = customer()
customerobj.customer_detail_input()
customerobj.database_customer()
