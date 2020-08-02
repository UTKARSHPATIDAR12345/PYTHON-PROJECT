#Importing Libraries

from class_customer import *
from class_purchase import *
from class_sale import *
from class_invoice import *
import sys

def menu():

    choice = 0
    while choice != 5:
        print('##########CHOOSE OPTIONS FROM BELOW#########\n')
        choice = int(input('''
                        1: CUSTOMERS DETAILS
                        2: SALE DETAILS
                        3: PURCHASE DETAILS
                        4: INVOICE DETAILS
                        5: QUIT    
                        Please Enter Your Choice :
            '''))
    #choice = 0    
    
        if choice == 1:
            #calling class_customer function
            print("\n##########CUSTOMERS DETAILS###########\n")
            cus = customer()
            cus.customer_detail_input()
            cus.database_customer()
    
        elif choice == 2:
            #calling class_sale function
            #time.sleep(2)
            print("\n##########SALE DETAILS###########\n")
            sell = sales()
            sell.input_customer()
            sell.input_company()
            sell.input_product()
            sell.products()
            sell.update_database()
        
        elif choice == 3:
            #calling class_purchase function
            #time.sleep(2)
            print("\n##########PURCHASE DETAILS###########\n")
            pur = purchase()
            pur.input_company()
            pur.input_product()
            pur.products()
            pur.update_purchase_database()
        
        elif choice == 4:
            #time.sleep(2)
            print("\n##########INVOICE DETAILS###########\n")
            bill = invoice()
            bill.customer_detail_input()
            bill.input_company()
            bill.input_product()
            bill.products()
            bill.update_invoice_database()
    
        elif choice == 5:
            sys.exit

        else:
            print('Invalid Choice')
            print('Please Select from 1, 2, 3, 4, 5')

menu()