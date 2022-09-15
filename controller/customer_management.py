from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import uic
from controller.history_window import history_window
from model.customer import Customer
from model.customerDAO import CustomerDAO

FILE_UI = 'view/customers_management.ui'

class Customer_ui(QWidget):
    def __init__(self):
        super(Customer_ui, self).__init__()
        uic.loadUi(FILE_UI, self)
        
        self.table.horizontalHeader().setStretchLastSection(True) 
        self.table.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch)
        
        self.Btn_Add.clicked.connect(self.add)
        self.Btn_Edit.clicked.connect(self.edit)
        self.Btn_Delete.clicked.connect(self.delete)
        
        self.Btn_History.clicked.connect(self.openHistory)
        self.winistory = None #Variável para guardar a referêncida da janela
        
        self.loadData()
        
    def loadData(self):
        items_lst = CustomerDAO.selectALL()
        for c in items_lst:
            self.addTableItem(c)
        
    def openHistory(self):
        self.winHistory = history_window()
        self.winHistory.show()
        
    def add(self):
        name = self.name.text()
        cpf = self.cpf.text()
        phone = self.phone.text()
        email = self.email.text()
        address = self.address.text()
        
        newItem = Customer(-1, name, cpf, phone, email, address)
        id = CustomerDAO.add(newItem)
        newItem.id = id
        
        self.addTableItem(newItem)
        self.name.clear()
        self.cpf.clear()
        self.phone.clear()
        self.email.clear()
        self.address.clear()
        
    def edit(self):
        pass

    def delete(self):
        lineSel = self.table.currentRow()
        lineItem = self.table.item(lineSel, 0)
        id = lineItem.text()
        self.table.removeRow(lineSel)
        CustomerDAO.delete(int(id))
            
        
    def addTableItem(self, c: Customer):
        line = self.table.rowCount()
        self.table.insertRow(line)
        id = QTableWidgetItem(str(c.id))
        name = QTableWidgetItem(c.name)
        cpf = QTableWidgetItem(c.cpf)
        phone = QTableWidgetItem(c.phone)
        email = QTableWidgetItem(c.email)
        address = QTableWidgetItem(c.address)
            
        self.table.setItem(line, 0, id)
        self.table.setItem(line, 1, name)
        self.table.setItem(line, 2, cpf)
        self.table.setItem(line, 3, phone)
        self.table.setItem(line, 4, email)
        self.table.setItem(line, 5, address)
