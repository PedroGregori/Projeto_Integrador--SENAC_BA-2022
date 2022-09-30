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

        quantity = self.findProduct.currentData().stock_quantity
        price = self.findProduct.currentData().salePrice
        print(self.findProduct.currentData().id)
        price = price.replace("R$", "").replace(",", ".")
        self.stockQuantity.setText(str(quantity))
        self.itemPrice.setValue(float(price))
