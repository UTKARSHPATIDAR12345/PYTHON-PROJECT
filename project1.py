from class_customer import *
from class_product_info import *
from class_purchase import *
from class_sale import *



sell = sales()
sell.input_customer()
sell.input_company()
sell.input_product()
sell.products()
sell.update_database()

pur=purchase()
pur.input_company()
pur.input_product()
pur.products()
pur.update_purchase_database()


cus=customer()
cus.customer_detail_input()
cus.database_customer()
