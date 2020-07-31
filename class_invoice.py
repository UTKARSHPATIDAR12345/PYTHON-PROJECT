import sqlite3
import datetime

now = datetime.datetime.now()
dt = now.strftime("%d/%m/%Y at %H:%M")

class product_info:
    
    mrp = 0.0
    pur_rate = 0.0
    exp_date = " "
    discount = 0.0
    final_price = 0.0

class invoice(product_info):

	def __init__(self):

		print('Inside Invoice')
		self.customer_name = " "
		self.contact_number = " "
		self.com_name = " "
		self.product_name = " "
		self.email = " "
		self.gstno = " "
		self.pack_size = " "
		self.product_code  = " "

	def customer_detail_input(self):

		print('CUSTOMER NAME : ')
		self.customer_name = input()

		print('CONTACT NUMBER : ')
		self.contact_number = input()

		print('GST NUMBER : ')
		self.gstno = input()

		print('EMAIL ADDRESS : ')
		self.email = input()

	def input_company(self):

		print('COMPANY NAME : ')
		self.com_name = input()

	def input_product(self):

		print('PRODUCT NAME : ')
		self.product_name = input()

		print('PRODUCT CODE : ')
		self.product_code = input()

		print('PACK SIZE : ')
		self.pack_size = input()

	def products(self):

		print('\nDETAILS OF PURCHASE AND SALE')
		
		print('RETAIL PRICE : ')
		self.mrp = input()
		
		print('SELLING PRICE : ')
		self.pur_rate = input()
		
		print('EXPIRY DATE : ')
		self.exp_date = input()
		
		print('DISCOUNT ')
		self.discount = input()

		print('FINAL PRICE : ')
		self.final_price = input()

	def update_invoice_database(self):

		connection_invoice = sqlite3.connect("PROJECT.db")
		cursor_invoice = connection_invoice.cursor()

		cursor_invoice.execute('''CREATE TABLE IF NOT EXISTS invoice(
    					ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    					Customer_Name VARCHAR(50) NOT NULL,
    					Contact_Number INT NOT NULL,
    					GST_Number INT NOT NULL,
    					Email REAL NOT NULL,
    					Company_Name VARCHAR(50) NOT NULL,
    					Product_Name VARCHAR(50) NOT NULL,
    					Product_Code VARCHAR(10) NOT NULL,
    					Pack_Size INT NOT NULL,
    					Retail_Price REAL NOT NULL,
    					Selling_Price REAL NOT NULL,
    					Discount REAL NOT NULL,
    					Expiry_Date REAL NOT NULL,
    					date_time REAL NOT NULL
    				)
    		''')
		cursor_invoice.execute("INSERT INTO invoice (Customer_Name, Contact_Number, GST_Number, Email, Company_Name, Product_Name, Product_Code, Pack_Size, Retail_Price, Selling_Price, Discount, Expiry_Date, date_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.customer_name, self.contact_number, self.gstno, self.email, self.com_name, self.product_name, self.product_code, self.pack_size, self.mrp, self.pur_rate, self.discount, self.exp_date, dt))

		connection_invoice.commit()
		connection_invoice.close()

