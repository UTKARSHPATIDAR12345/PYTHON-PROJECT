#Importing Libraries

from class_customer import *
from class_purchase import *
from class_sale import *
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
