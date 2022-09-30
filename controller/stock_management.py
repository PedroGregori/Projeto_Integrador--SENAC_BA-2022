from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import QDate
from model.purschaseHistory import purchaseHistory
from model.stock import Stock
from model.stockDAO import Stock_DAO
from controller.purchase_history import History_ui

FILE_UI = "view/management UIs/stock_management.ui"


class Stock_ui(QWidget):
    
    def __init__(self):
        super(Stock_ui, self).__init__()
        uic.loadUi(FILE_UI, self)

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents)

        self.Btn_add.clicked.connect(self.add_provider)
        self.Btn_edit.clicked.connect(self.edit)
        self.Btn_delete.clicked.connect(self.delete)
        self.Btn_buy.clicked.connect(self.buy)
        #self.Btn_history.clicked.connect(self.openHistory)
        self.Btn_history.setEnabled(False)
        
        self.table.cellClicked.connect(self.updateUiCellClick)

        self.loadData()

        self.search.textEdited.connect(self.loadData)

    def loadData(self, text=''):
        self.table.setRowCount(0)
        items_lst = Stock_DAO.selectALL(text)
        for s in items_lst:
            self.addTableItem(s)
        purchases_lst = Stock_DAO.ALLpurchases()
        for p in purchases_lst:
            self.updateDate(p)
            

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
        
    def clearFields(self):
        self.provider.clear()
        self.product.clear()
        self.purchaseCost.setValue(0.00)
        self.salePrice.setValue(0.00)
        self.quantity.setValue(0.00)
    
    def updateUiCellClick(self):
        lineSel = self.table.currentRow()

        purchaseCost = self.table.item(lineSel, 4).text()
        salePrice = self.table.item(lineSel, 6).text()
        purchaseCost = purchaseCost.replace("R$", "").replace(",", ".")
        salePrice = salePrice.replace("R$", "").replace(",", ".")

        self.provider.setText(self.table.item(lineSel, 1).text())
        self.product.setText(self.table.item(lineSel, 2).text())
        self.purchaseCost.setValue(float(purchaseCost))
        self.salePrice.setValue(float(salePrice))
        
    def add_provider(self):
        provider = self.provider.text()
        product = self.product.text()
        purchaseCost = self.purchaseCost.text()
        stock_quantity = 0
        lastPurchase = "Nenhuma compra"
        salePrice = self.salePrice.text()

        newProvider = Stock(-1, provider, product, purchaseCost,
                            stock_quantity, lastPurchase, salePrice)
        id = Stock_DAO.add(newProvider)
        newProvider.id = id
        self.addTableItem(newProvider)
        self.clearFields()

    def edit(self):
        lineSel = self.table.currentRow()
        id = self.table.item(lineSel, 0).text()
        provider = self.provider.text()
        product = self.product.text()
        purchaseCost = self.purchaseCost.text()
        lastPurchase = self.table.item(lineSel, 5).text()
        stock = self.table.item(lineSel, 3).text()
        salePrice = self.salePrice.text()
        
        editProvider = Stock(id, provider, product, purchaseCost, stock, lastPurchase, salePrice)
        Stock_DAO.edit(editProvider)
        self.updateTable(editProvider)
        self.clearFields()

    def delete(self):
        lineSel = self.table.currentRow()
        id = self.table.item(lineSel, 0).text()
        Stock_DAO.delete(int(id))
        self.clearFields()
        self.loadData()

    def buy(self):
        lineSel = self.table.currentRow()
        line = self.table.item(lineSel, 0)
        now = QDate.currentDate()
        providerID = line.text()
        quantity = self.quantity.text()
        purchaseDate = now.toString("dd-MM-yyyy")
        newPurchase = purchaseHistory(-1, providerID, quantity, purchaseDate)
        id = Stock_DAO.newPurchase(newPurchase)
        newPurchase.id = id
        Stock_DAO.addToStock(newPurchase)
        self.updateDate(newPurchase)
        self.loadData()
        self.clearFields()

    def openHistory(self):
        lineSel = self.table.currentRow()
        if lineSel != None:
            id = self.table.item(lineSel, 0).text()
            self.winHistory = History_ui(int(id))
            self.winHistory.show()

    def addTableItem(self, s: Stock):
        line = self.table.rowCount()
        self.table.insertRow(line)

        id = QTableWidgetItem(str(s.id))
        provider = QTableWidgetItem(s.provider)
        product = QTableWidgetItem(s.product)
        purchaseCost = QTableWidgetItem(str(s.purchaseCost))
        stock_quantity = QTableWidgetItem(str(s.stock_quantity))
        lastPurchase = QTableWidgetItem(s.lastPurchase)
        salePrice = QTableWidgetItem(str(s.salePrice))

        self.table.setItem(line, 0, id)
        self.table.setItem(line, 1, provider)
        self.table.setItem(line, 2, product)
        self.table.setItem(line, 3, stock_quantity)
        self.table.setItem(line, 4, purchaseCost)
        self.table.setItem(line, 5, lastPurchase)
        self.table.setItem(line, 6, salePrice)

    def updateTable(self, s: Stock):
        lineSel = self.table.currentRow()

        provider = QTableWidgetItem(s.provider)
        product = QTableWidgetItem(s.product)
        purchaseCost = QTableWidgetItem(str(s.purchaseCost))
        salePrice = QTableWidgetItem(str(s.salePrice))

        self.table.setItem(lineSel, 1, provider)
        self.table.setItem(lineSel, 2, product)
        self.table.setItem(lineSel, 4, purchaseCost)
        self.table.setItem(lineSel, 6, salePrice)

    def updateDate(self, p: purchaseHistory):
        lineSel = self.table.currentRow()
        purchaseDate = QTableWidgetItem(p.purchaseDate)
        self.table.setItem(lineSel, 5, purchaseDate)
