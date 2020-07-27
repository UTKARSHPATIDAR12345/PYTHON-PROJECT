#Importing Libraries

from class_customer import *
from class_purchase import *
from class_sale import *

#calling class_customer function
print("##########CUSTOMERS DETAILS###########")
cus = customer()
cus.customer_detail_input()
cus.database_customer()

#calling class_sale function
print("##########SALE DETAILS###########")
sell = sales()
sell.input_customer()
sell.input_company()
sell.input_product()
sell.products()
sell.update_database()

#calling class_purchase function
print("##########PURCHASE DETAILS###########")
pur = purchase()
pur.input_company()
pur.input_product()
pur.products()
pur.update_purchase_database()

