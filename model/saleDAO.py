from .db import connect
from .sale import Sale
from .saleItems import SaleItems
from .customer import Customer
from .stock import Stock

class Sale_DAO():
    
    def getCustomers():
        customers_lst = []
        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT * FROM customers;" 
        cursor.execute(SQL)
        return_list = cursor.fetchall()
        for c  in return_list:
            customersData = Customer(c[0], c[1], c[2], c[3], c[4], c[5])
            customers_lst.append(customersData)
                
        conn.close()
            
        return customers_lst
    
    def getProducts():
        products_lst = []
        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT * FROM customers;" 
        cursor.execute(SQL)
        return_list = cursor.fetchall()
        for p  in return_list:
            productData = Stock(p[0], p[1], p[2], p[3], p[4], p[5], p[6])
            products_lst.append(productData)
                
        conn.close()
            
        return products_lst 
    
    def cadSale(s: Sale):
        