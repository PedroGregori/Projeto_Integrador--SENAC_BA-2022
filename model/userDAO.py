from .db import connect
from .user import User


class User_DAO():
    def add(u: User):
        conn = connect()
        cursor = conn.cursor()
        SQL = "INSERT INTO users(name, cpf, rg, address, salary, user, password, phone, email, userType) VALUES (?,?,?,?,?,?,?,?,?,?);"
        data = [u.name, u.cpf, u.rg, u.address, u.salary,
                u.user, u.password, u.phone, u.email, u.userType]
        cursor.execute(SQL, data)
        id_return = cursor.execute("SELECT last_insert_rowid();")
        id = id_return.fetchall()[0][0]
        conn.commit()
        conn.close()

        return id

    def edit(u: User):
        conn = connect()
        cursor = conn.cursor()
        SQL = "UPDATE users SET name=?, cpf=?, rg=?, address=?, salary=?, user=?, password=?, phone=?, email=?, userType=? WHERE id=?;"
        data = [u.name, u.cpf, u.rg, u.address, u.salary, u.user,
                u.password, u.phone, u.email, u.userType, u.id]
        cursor.execute(SQL, data)
        conn.commit()
        conn.close()

    def delete(id: int):
        conn = connect()
        cursor = conn.cursor()
        SQL = "DELETE FROM users WHERE id=?;"
        cursor.execute(SQL, [id])
        conn.commit()
        conn.close()

    def selectALL(textSearch=''):
        users_lst = []
        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT * FROM users WHERE name LIKE ?;"
        textSearch = '%' + textSearch + '%'
        cursor.execute(SQL, [textSearch])
        return_list = cursor.fetchall()
        for u in return_list:
            newUser = User(u[0], u[1], u[2], u[3], u[4], u[5],
                           u[6], u[7], u[8], u[9], u[10])
            users_lst.append(newUser)

        conn.close()

        return users_lst
