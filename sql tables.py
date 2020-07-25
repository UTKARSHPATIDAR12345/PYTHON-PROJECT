import sqlite3

connection_company=sqlite3.connect("COMPANY_TABLE.db")

cursor_company=connection_company.cursor()

cursor_company.execute('''CREATE TABLE IF NOT EXISTS company_table(   
  
COMPANY_NAME VARCHAR(30),
PRODUCT_NAME VARCHAR(30),
mrp integer,
purchaserate integer,
expdate text NOT NULL
) 
''')

cursor_company.execute("""INSERT INTO company_table VALUES ("AGAPPE", "BIO-CHEMISTRY", 150,50, "2021-03-28");""") 

connection_company.commit()

connection_company.close()

#####################################################COMPANY TABLE#############################################


connection_sale=sqlite3.connect("SALE_TABLE.db")

cursor_sale=connection_sale.cursor()

cursor_sale.execute('''CREATE TABLE IF NOT EXISTS sale(   
productname VARCHAR(30),  
companyname VARCHAR(30),
cutomername VARCHAR(30),
mrp integer,
purchaserate integer,
salerate float,
expdate text NOT NULL,
discount float,
finalrate float
) 
''')




cursor_sale.execute("""INSERT INTO sale VALUES ("BIO-CHEMISTRY", "AGAPPE", "AADARSH", 150,50,230, "2021-03-28",10,220);""") 

connection_sale.commit()

connection_sale.close()



