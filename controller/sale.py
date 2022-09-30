from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic
from model.saleDAO import Sale_DAO
from model.saleOBJ import Sale

FILE_UI = 'view/sell.ui'


class Sale_ui(QWidget):

    saleUiConnect = pyqtSignal()

    def __init__(self, user):
        super(Sale_ui, self).__init__()
        uic.loadUi(FILE_UI, self)

        self.user = user
        self.attendantLabel.setText(f"Atendente: {self.user}")

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents)

        self.Btn_newCustomer.clicked.connect(lambda: self.saleUiConnect.emit())
        self.Btn_select.clicked.connect(self.select)
        self.Btn_add.clicked.connect(self.add)
        self.getData()

    def clearData(self):
        self.customer.clear()
        self.findProduct.clear()

    def getData(self):
        self.clearData()
        customer_lst = Sale_DAO.getCustomers()
        for item in customer_lst:
            self.customer.addItem(item.name, item)

        products_lst = Sale_DAO.getProducts()
        for item in products_lst:
            self.findProduct.addItem(item.product, item)

    def select(self):
        quantity = self.findProduct.currentData().stock_quantity
        price = self.findProduct.currentData().salePrice
        price = price.replace("R$", "").replace(",", ".")
        self.stockQuantity.setText(str(quantity))
        self.itemPrice.setValue(float(price))
        return float(price)
    
    def cadSale(self):
        pass
    
    def add(self):
        price = self.findProduct.currentData().salePrice
        customer = self.customer.currentData().name
        product = self.findProduct.currentData().product
        quantity = self.productsQuantity.text()
        itemsPrice = int(quantity)*self.select()
        self.itemsValue.setValue(itemsPrice)
        
        line = self.table.rowCount()
        self.table.insertRow(line)
        
        item = QTableWidgetItem(product)
        itemsQuantity = QTableWidgetItem(quantity)
        price = QTableWidgetItem(price)

        self.table.setItem(line, 0, item)
        self.table.setItem(line, 1, itemsQuantity)
        self.table.setItem(line, 2, price)
