import sqlite3

class customer:
    customer_name=" "
    contact_number=" "
    gstno=" "
    address=" "
    customer_debit=0

    def customer_detail_input(self):
        print("PLEASE ENTER THE NAME OF THE CUSTOMER")
        self.customer_name=input()
        print("PLEASE ENTER THE CONTACT NUMBER OF THE CUSTOMER")
        self.customer_number=input()
        print("PLEASE ENTER THE GST.NO OF THE CUSTOMER")
        self.gstno=input()
        print("PLEASE ENTER THE ADDRESS OF THE CUSTOMER")
        self.address=input()
        
    def database_customer(self):
        connection_customer=sqlite3.connect("CUSTOMER.db")

        cursor_customer=connection_customer.cursor()

        cursor_customer.execute('''CREATE TABLE IF NOT EXISTS customer(
            customer_number TEXT NOT NULL,
            customer_gst_number TEXT NOT NULL,
            customer_address TEXT NOT NULL
        )'''
        )

        cursor_customer.execute('''INSERT INTO customer(customer_number,customer_gst_number,customer_address) VALUES(?,?,?)''',
        (self.customer_number,self.gstno,self.address)
        )

        connection_customer.commit()

        connection_customer.close()


customerobj=customer()
customerobj.customer_detail_input()
customerobj.database_customer()