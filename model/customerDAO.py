from .db import connect
from .customer import Customer

class CustomerDAO():
    def add(c: Customer):
        conn = connect()
        cursor = conn.cursor()
        SQL = "INSERT INTO customers(name, cpf, phone, email, address) VALUES (?,?,?,?,?);"
        data = [c.name, c.cpf, c.phone, c.email, c.address] 
        cursor.execute(SQL, data)
        id_return = cursor.execute("SELECT last_insert_rowid();")
        id = id_return.fetchall()[0] [0]
        conn.commit()
        conn.close()
            
        return id

    def edit(c: Customer):
        conn = connect()
        cursor = conn.cursor()
        SQL = "UPDATE customers SET name=?, cpf=?, phone=?, email=?, address=? WHERE id=?;"
        data = [c.name, c.cpf, c.phone, c.email, c.address, c.id] 
        cursor.execute(SQL, data)
        conn.commit()
        conn.close()

    def delete(id: int):
        conn = connect()
        cursor = conn.cursor()
        SQL = "DELETE FROM customers WHERE id=?;"
        cursor.execute(SQL,[id])
        conn.commit()
        conn.close()

    def selectALL():
        customers_lst = []
        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT * FROM customers;"
        cursor.execute(SQL)
        return_list = cursor.fetchall()
        for c  in return_list:
            newCustomer = Customer(c[0], c[1] ,c[2], c[3], c[4], c[5])
            customers_lst.append(newCustomer)
                
        conn.close()
            
        return customers_lst