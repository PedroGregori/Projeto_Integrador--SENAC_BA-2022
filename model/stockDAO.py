from .db import connect
from .stock import Stock

class Stock_DAO():
    
    def add(s: Stock):
        conn = connect()
        cursor = conn.cursor()
        SQL = "INSERT INTO stock(provider, product, purchaseCost, stock_quantity, salePrice) VALUES (?,?,?,?);"
        data = [s.provider, s.product, s.purchaseCost, s.stock_quantity, s.salePrice] 
        cursor.execute(SQL, data)
        id_return = cursor.execute("SELECT last_insert_rowid();")
        id = id_return.fetchall()[0] [0]
        conn.commit()
        conn.close()
            
        return id

    def edit(s: Stock):
        conn = connect()
        cursor = conn.cursor()
        SQL = "UPDATE stock SET provider=?, product=?, purchaseCost=?, stock_quantity=?, salePrice=? WHERE id=?;"
        data = [s.provider, s.product, s.purchaseCost, s.stock_quantity, s.salePrice, s.id] 
        cursor.execute(SQL, data)
        conn.commit()
        conn.close()

    def delete(id: int):
        conn = connect()
        cursor = conn.cursor()
        SQL = "DELETE FROM stock WHERE id=?;"
        cursor.execute(SQL,[id])
        conn.commit()
        conn.close()

    def selectALL(textSearch=''):
        stock_lst = []
        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT * FROM stock WHERE provider LIKE ?;"
        textSearch = '%' + textSearch +'%' 
        cursor.execute(SQL, [textSearch])
        return_list = cursor.fetchall()
        for p  in return_list:
            newProvider = Stock(p[0], p[1] ,p[2], p[3], p[4])
            stock_lst.append(newProvider)
                
        conn.close()
            
        return stock_lst