from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PyQt5 import uic
from model.userDAO import User_DAO
from model.user import User

FILE_UI = "view/management UIs/users_management.ui"


class Users_ui(QWidget):
    def __init__(self):
        super(Users_ui, self).__init__()
        uic.loadUi(FILE_UI, self)

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents)

        self.Btn_add.clicked.connect(self.add)
        self.Btn_edit.clicked.connect(self.edit)
        self.Btn_delete.clicked.connect(self.delete)

        self.table.cellClicked.connect(self.updateUiCellClick)

        self.loadData()

        self.search.textEdited.connect(self.loadData)

    def loadData(self, text=''):
        self.table.setRowCount(0)
        items_lst = User_DAO.selectALL(text)
        for u in items_lst:
            self.addTableItem(u)

    def clearFields(self):
        self.name.clear()
        self.cpf.clear()
        self.rg.clear()
        self.address.clear()
        self.user.clear()
        self.password.clear()
        self.email.clear()
        self.phone.clear()

    def confirm_dialog(self, msg):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Confrimação")
        dlg.setText(msg)
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            return 'yes'
        else:
            return 'no'

    def updateUiCellClick(self):
        lineSel = self.table.currentRow()

        salaryValue = self.table.item(lineSel, 5).text()
        salaryValue = salaryValue.replace("R$", "")
        salaryValue = salaryValue.replace(",", ".")

        self.name.setText(self.table.item(lineSel, 1).text())
        self.cpf.setText(self.table.item(lineSel, 2).text())
        self.rg.setText(self.table.item(lineSel, 3).text())
        self.address.setText(self.table.item(lineSel, 4).text())
        self.salary.setValue(float(salaryValue))
        self.user.setText(self.table.item(lineSel, 6).text())
        self.password.setText(self.table.item(lineSel, 7).text())
        self.email.setText(self.table.item(lineSel, 8).text())
        self.phone.setText(self.table.item(lineSel, 9).text())
        text = self.table.item(lineSel, 10).text()
        
        index = self.userType.findText(text)
        if index >= 0:
            self.userType.setCurrentIndex(index)
    def emptyFieldsAlert(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Aviso")
        dlg.setText('Preencha o resto dos campos!')
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Warning)
        dlg.exec()

    def add(self):
        name = self.name.text()
        cpf = self.cpf.text()
        rg = self.rg.text()
        address = self.address.text()
        salary = self.salary.text()
        user = self.user.text()
        password = self.password.text()
        email = self.email.text()
        phone = self.phone.text()
        userType = self.userType.currentText()

        salary = salary.replace("R$", "")

        newUser = User(-1, name, cpf, rg, address, salary,
                       user, password, email, phone, userType)
        if name == "" or cpf == "" or rg == "" or address == "" or user == "" or password == "" or email == "" or phone == "":
            self.emptyFieldsAlert()
        else:
            id = User_DAO.add(newUser)
            newUser.id = id
            self.addTableItem(newUser)
            self.clearFields()

    def edit(self):
        lineSel = self.table.currentRow()
        line = self.table.item(lineSel, 0)
        id = line.text()
        name = self.name.text()
        cpf = self.cpf.text()
        rg = self.rg.text()
        address = self.address.text()
        salary = self.salary.text()
        user = self.user.text()
        password = self.password.text()
        email = self.email.text()
        phone = self.phone.text()
        userType = self.userType.currentText()

        editUser = User(id, name, cpf, rg, address, salary,
                        user, password, email, phone, userType)
        if name == "" or cpf == "" or rg == "" or address == "" or user == "" or password == "" or email == "" or phone == "":
            self.emptyFieldsAlert()
        else:
            User_DAO.edit(editUser)
            self.updateTable(editUser)
            self.clearFields()

    def delete(self):
        lineSel = self.table.currentRow()
        lineItem = self.table.item(lineSel, 0)
        id = lineItem.text()
        confirm = self.confirm_dialog(
            'Tem certeza que deseja excluir? ESTA AÇÃO É IRREVERSÍVEL!')
        if confirm == 'yes':
            self.table.removeRow(lineSel)
            User_DAO.delete(int(id))
        self.clearFields()

    def addTableItem(self, u: User):
        line = self.table.rowCount()
        self.table.insertRow(line)

        salary = "R$ " + u.salary
        id = QTableWidgetItem(str(u.id))
        name = QTableWidgetItem(u.name)
        cpf = QTableWidgetItem(u.cpf)
        rg = QTableWidgetItem(str(u.rg))
        address = QTableWidgetItem(u.address)
        salary = QTableWidgetItem(salary)
        user = QTableWidgetItem(u.user)
        password = QTableWidgetItem(u.password)
        email = QTableWidgetItem(u.email)
        phone = QTableWidgetItem(str(u.phone))
        userType = QTableWidgetItem(u.userType)

        self.table.setItem(line, 0, id)
        self.table.setItem(line, 1, name)
        self.table.setItem(line, 2, cpf)
        self.table.setItem(line, 3, rg)
        self.table.setItem(line, 4, address)
        self.table.setItem(line, 5, salary)
        self.table.setItem(line, 6, user)
        self.table.setItem(line, 7, password)
        self.table.setItem(line, 8, email)
        self.table.setItem(line, 9, phone)
        self.table.setItem(line, 10, userType)

    def updateTable(self, u: User):
        lineSel = self.table.currentRow()
        salary = "R$ " + u.salary
        name = QTableWidgetItem(u.name)
        cpf = QTableWidgetItem(u.cpf)
        rg = QTableWidgetItem(str(u.rg))
        address = QTableWidgetItem(u.address)
        salary = QTableWidgetItem(salary)
        user = QTableWidgetItem(u.user)
        password = QTableWidgetItem(u.password)
        email = QTableWidgetItem(u.email)
        phone = QTableWidgetItem(str(u.phone))
        userType = QTableWidgetItem(u.userType)

        self.table.setItem(lineSel, 1, name)
        self.table.setItem(lineSel, 2, cpf)
        self.table.setItem(lineSel, 3, rg)
        self.table.setItem(lineSel, 4, address)
        self.table.setItem(lineSel, 5, salary)
        self.table.setItem(lineSel, 6, user)
        self.table.setItem(lineSel, 7, password)
        self.table.setItem(lineSel, 8, email)
        self.table.setItem(lineSel, 9, phone)
        self.table.setItem(lineSel, 10, userType)
