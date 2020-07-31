#Importing Libraries

from class_customer import *
from class_purchase import *
from class_sale import *
from class_invoice import *
import time

#calling class_customer function
print("\n##########CUSTOMERS DETAILS###########\n")
cus = customer()
cus.customer_detail_input()
cus.database_customer()

#calling class_sale function
time.sleep(2)
print("\n##########SALE DETAILS###########\n")
sell = sales()
sell.input_customer()
sell.input_company()
sell.input_product()
sell.products()
sell.update_database()

#calling class_purchase function
time.sleep(2)
print("\n##########PURCHASE DETAILS###########\n")
pur = purchase()
pur.input_company()
pur.input_product()
pur.products()
pur.update_purchase_database()

time.sleep(2)
print("\n##########INVOICE DETAILS###########\n")
bill = invoice()
bill.customer_detail_input()
bill.input_company()
bill.input_product()
bill.products()
bill.update_invoice_database()
