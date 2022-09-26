from .db import connect
from .provider import Provider

class Provider_DAO():
    
    def add(p: Provider):
        conn = connect()
        cursor = conn.cursor()
        SQL = "INSERT INTO providers(provider, product, quantity, purchaseDate, purchaseCost, salePrice) VALUES (?,?,?,?,?,?);"
        data = [p.provider, p.product, p.quantity, p.purchaseDate, p.purchaseCost, p.salePrice] 
        cursor.execute(SQL, data)
        id_return = cursor.execute("SELECT last_insert_rowid();")
        id = id_return.fetchall()[0] [0]
        conn.commit()
        conn.close()
            
        return id

    def edit(p: Provider):
        conn = connect()
        cursor = conn.cursor()
        SQL = "UPDATE providers SET provider=?, product=?, quantity=?, purchaseDate=?, purchaseCost=?, salePrice=? WHERE id=?;"
        data = [p.provider, p.product, p.quantity, p.purchaseDate, p.purchaseCost, p.salePrice, p.id] 
        cursor.execute(SQL, data)
        conn.commit()
        conn.close()

    def delete(id: int):
        conn = connect()
        cursor = conn.cursor()
        SQL = "DELETE FROM providers WHERE id=?;"
        cursor.execute(SQL,[id])
        conn.commit()
        conn.close()

    def selectALL(textSearch=''):
        providers_lst = []
        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT * FROM providers WHERE provider LIKE ?;"
        textSearch = '%' + textSearch +'%' 
        cursor.execute(SQL, [textSearch])
        return_list = cursor.fetchall()
        for p  in return_list:
            newProvider = Provider(p[0], p[1] ,p[2], p[3], p[4], p[5], p[6])
            providers_lst.append(newProvider)
                
        conn.close()
            
        return providers_lst