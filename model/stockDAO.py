from .db import connect
from .stock import Stock
from .purschaseHistory import purchaseHistory


class Stock_DAO():

    def add(s: Stock):
        conn = connect()
        cursor = conn.cursor()
        SQL = "INSERT INTO stock(provider, product, purchaseCost, stock_quantity, lastPurchase, salePrice) VALUES (?,?,?,?,?,?);"
        data = [s.provider, s.product, s.purchaseCost,
                s.stock_quantity, s.lastPurchase, s.salePrice]
        cursor.execute(SQL, data)
        id_return = cursor.execute("SELECT last_insert_rowid();")
        id = id_return.fetchall()[0][0]
        conn.commit()
        conn.close()

        return id

    def edit(s: Stock):
        conn = connect()
        cursor = conn.cursor()
        SQL = "UPDATE stock SET provider=?, product=?, purchaseCost=?, salePrice=? WHERE id=?;"
        data = [s.provider, s.product, s.purchaseCost, s.salePrice, s.id]
        cursor.execute(SQL, data)
        conn.commit()
        conn.close()

    def delete(id: int):
        conn = connect()
        cursor = conn.cursor()
        SQL = "DELETE FROM stock WHERE id=?;"
        cursor.execute(SQL, [id])
        conn.commit()
        SQL = "DELETE FROM purchase_history WHERE providerID=?;"
        cursor.execute(SQL, [id])
        conn.commit()        
        conn.close()

    def selectALL(textSearch=''):
        stock_lst = []
        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT * FROM stock WHERE provider LIKE ?;"
        textSearch = '%' + textSearch + '%'
        cursor.execute(SQL, [textSearch])
        return_list = cursor.fetchall()
        for p in return_list:
            newProvider = Stock(p[0], p[1], p[2], p[3], p[4], p[5], p[6])
            stock_lst.append(newProvider)

        conn.close()

        return stock_lst

    def newPurchase(p: purchaseHistory):
        conn = connect()
        cursor = conn.cursor()
        SQL = "INSERT INTO purchase_history(providerID, quantity, purchaseDate) VALUES (?,?,?);"
        data = [p.providerID, p.quantity, p.purchaseDate]
        cursor.execute(SQL, data)
        id_return = cursor.execute("SELECT last_insert_rowid();")
        id = id_return.fetchall()[0][0]
        conn.commit()
        conn.close()

        return id

    def addToStock(p: purchaseHistory):
        conn = connect()
        cursor = conn.cursor()
        SQL = "UPDATE stock SET lastPurchase=?, stock_quantity=(SELECT stock_quantity FROM stock WHERE id=?)+? WHERE id=?"
        data = [p.purchaseDate, p.providerID, p.quantity, p.providerID]
        cursor.execute(SQL, data)
        conn.commit()
        conn.close()

    def getProvider(id: purchaseHistory):
        provider_lst = []
        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT * FROM stock WHERE id=?"
        data = [id.providerID]
        cursor.execute(SQL, data)
        return_provider = cursor.fetchall()
        for p in return_provider:
            provider = Stock(p[0], p[1], p[2], p[3], p[4])
            provider_lst.append(provider)

        conn.close()

        return provider_lst

    def ALLpurchases():
        purchase_lst = []
        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT * FROM purchase_history"
        cursor.execute(SQL)
        return_lst = cursor.fetchall()
        for p in return_lst:
            newPurchase = purchaseHistory(p[0], p[1], p[2], p[3])
            purchase_lst.append(newPurchase)

        conn.close()

        return purchase_lst
