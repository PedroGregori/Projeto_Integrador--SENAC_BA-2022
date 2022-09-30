from .db import connect
from .saleOBJ import Sale
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
        SQL = "SELECT * FROM stock;" 
        cursor.execute(SQL)
        return_list = cursor.fetchall()
        for p  in return_list:
            productData = Stock(p[0], p[1], p[2], p[3], p[4], p[5], p[6])
            products_lst.append(productData)
                
        conn.close()
            
        return products_lst 
    
    def cadSale(s: Sale):
        conn = connect()
        cursor = conn.cursor()
        SQL = "INSERT INTO sales(customerID, attendant, totalValue, valueReiceived, saleDate) VALUE (?,?,?,?,?);"
        data = [s.customerID, s.attendant, s.totalValue, s.valueReceived, s.saleDate]
        cursor.execute(SQL, data)
        id_return = cursor.execute("SELECT last_insert_rowid();")
        id = id_return.fetchall()[0] [0]
        conn.commit()
        
        SQL = "INSERT INTO saleItems(productID, items_quantity) VALUE (?,?);"
        data = [s.productID, s.items_quantity]
        cursor.execute(SQL, data)
        conn.commit()
        conn.close()
            
        return id
    
    def getFromStock(s: Sale):
        conn = connect()
        cursor = conn.cursor()
        SQL = "UPDATE stock SET stock_quantity=(SELECT stock_quantity FROM stock WHERE id=?)-? WHERE id=?"
        data = [s.productID, s.items_quantity, s.productID]
        cursor.execute(SQL, data)
        conn.commit()
        conn.close()