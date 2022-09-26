from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PyQt5 import uic
from controller.history_window import history_window
from model.customer import Customer
from model.customerDAO import Customer_DAO

FILE_UI = 'view/management UIs/customers_management.ui'


class Customer_ui(QWidget):
    def __init__(self):
        super(Customer_ui, self).__init__()
        uic.loadUi(FILE_UI, self)

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents)

        self.Btn_Add.clicked.connect(self.add)
        self.Btn_Edit.clicked.connect(self.edit)
        self.Btn_Delete.clicked.connect(self.delete)
        self.Btn_History.clicked.connect(self.openHistory)
        self.winistory = None  # Variável para guardar a referêncida da janela

        self.table.cellClicked.connect(self.updateUiCellClick)

        self.loadData()

        self.search.textEdited.connect(self.loadData)

    def loadData(self, text=''):
        self.table.setRowCount(0)
        items_lst = Customer_DAO.selectALL(text)
        for c in items_lst:
            self.addTableItem(c)

    def clearFields(self):
        self.name.clear()
        self.cpf.clear()
        self.phone.clear()
        self.email.clear()
        self.address.clear()

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

    def openHistory(self):
        self.winHistory = history_window()
        self.winHistory.show()

    def updateUiCellClick(self):
        lineSel = self.table.currentRow()

        self.name.setText(self.table.item(lineSel, 1).text())
        self.cpf.setText(self.table.item(lineSel, 2).text())
        self.phone.setText(self.table.item(lineSel, 3).text())
        self.email.setText(self.table.item(lineSel, 4).text())
        self.address.setText(self.table.item(lineSel, 5).text())

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
        phone = self.phone.text()
        email = self.email.text()
        address = self.address.text()

        if name == "" or cpf == "" or phone == "" or address == "":
            self.emptyFieldsAlert()

        else:
            newItem = Customer(-1, name, cpf, phone, email, address)
            id = Customer_DAO.add(newItem)
            newItem.id = id

            self.addTableItem(newItem)
            self.clearFields()

    def edit(self):
        lineSel = self.table.currentRow()
        lineItem = self.table.item(lineSel, 0)
        if lineItem == None:
            print('nenhum selecioando')
        else:
            id = lineItem.text()
        name = self.name.text()
        cpf = self.cpf.text()
        phone = self.phone.text()
        email = self.email.text()
        address = self.address.text()

        if name == "" or cpf == "" or phone == "" or address == "":
            self.emptyFieldsAlert()

        else:
            newItem = Customer(id, name, cpf, phone, email, address)
            self.updateTable(newItem)
            Customer_DAO.edit(newItem)

            self.clearFields()

    def delete(self):
        lineSel = self.table.currentRow()
        lineItem = self.table.item(lineSel, 0)
        id = lineItem.text()
        confirm = self.confirm_dialog(
            "Tem certeza que deseja excluir? ESTA AÇÃO É IRREVERSÍVEL!")
        if confirm == 'yes':
            self.table.removeRow(lineSel)
            Customer_DAO.delete(int(id))

        self.clearFields()

    def addTableItem(self, c: Customer):
        line = self.table.rowCount()
        self.table.insertRow(line)
        id = QTableWidgetItem(str(c.id))
        name = QTableWidgetItem(c.name)
        cpf = QTableWidgetItem(str(c.cpf))
        phone = QTableWidgetItem(str(c.phone))
        email = QTableWidgetItem(c.email)
        address = QTableWidgetItem(c.address)

        self.table.setItem(line, 0, id)
        self.table.setItem(line, 1, name)
        self.table.setItem(line, 2, cpf)
        self.table.setItem(line, 3, phone)
        self.table.setItem(line, 4, email)
        self.table.setItem(line, 5, address)

    def updateTable(self, c: Customer):
        lineSel = self.table.currentRow()
        name = QTableWidgetItem(c.name)
        cpf = QTableWidgetItem(str(c.cpf))
        phone = QTableWidgetItem(str(c.phone))
        email = QTableWidgetItem(c.email)
        address = QTableWidgetItem(c.address)

        self.table.setItem(lineSel, 1, name)
        self.table.setItem(lineSel, 2, cpf)
        self.table.setItem(lineSel, 3, phone)
        self.table.setItem(lineSel, 4, email)
        self.table.setItem(lineSel, 5, address)
