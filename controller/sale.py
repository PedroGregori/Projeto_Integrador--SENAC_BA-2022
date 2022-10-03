from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PyQt5.QtCore import pyqtSignal, QDate
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
        self.Btn_add.clicked.connect(self.add)
        self.Btn_finish.clicked.connect(self.cadSale)
        self.findProduct.activated.connect(self.select)
        self.customer.activated.connect(self.select)
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

    def emptyFieldsAlert(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Aviso")
        dlg.setText('Escolha uma quantidade de produtos')
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Warning)
        dlg.exec()
    
    def add(self):
        quantity = int(self.productsQuantity.text())

        if quantity == 0:
            self.emptyFieldsAlert()
            
        itemsPrice = int(quantity)*self.select()
        self.itemsValue.setValue(itemsPrice)
        stock = int(self.stockQuantity.text())
        getStock = stock-quantity
        updateStock = str(getStock)
        self.stockQuantity.setText(updateStock)
                
        customerID = self.customer.currentData().id
        productID = self.findProduct.currentData().id
        attendant = self.attendantLabel.text()
        
        now = QDate.currentDate()
        saleDate = now.toString("dd-MM-yyyy")
        
        totalValue =+ itemsPrice
        
        sale = Sale(-1, customerID, attendant, totalValue, -1, productID, int(quantity), saleDate)
        self.addTable(sale)
        return sale

    def addTable(self, s: Sale):
        price = self.findProduct.currentData().salePrice
        product = self.findProduct.currentData().product
        
        line = self.table.rowCount()
        self.table.insertRow(line)
        
        item = QTableWidgetItem(product)
        itemsQuantity = QTableWidgetItem(str(s.items_quantity))
        price = QTableWidgetItem(price)

        self.table.setItem(line, 0, item)
        self.table.setItem(line, 1, itemsQuantity)
        self.table.setItem(line, 2, price)

    def delete(self):
        lineSel = self.table.currentRow()
        self.table.lineSel.removeRow()    
    
    def cadSale(self):
        saleData = self.add()
        valueReceived = self.valueReceived.text()
        saleData.valueReceived = valueReceived
        totalValue = saleData.totalValue
        self.totalValue.setValue(totalValue)
        Sale_DAO.getFromStock(saleData)
        