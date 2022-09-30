from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import uic
from model.purschaseHistory import purchaseHistory
from model.stock import Stock
from model.stockDAO import Stock_DAO


FILE_UI = "view/history.ui"


class History_ui(QWidget):
    
    def __init__(self, id):
        super(History_ui, self).__init__()
        uic.loadUi(FILE_UI, self)
        
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents)
        self.getHistory(id)
        
    def getHistory(self,id):
        purchases = Stock_DAO.showPurchases(id)
        p = purchases[0]
        product = Stock_DAO.getProvider(p.providerID)
        
        self.addTableItem(purchases, product)
        
    def addTableItem(self, p: purchaseHistory, s: Stock):
        line = self.table.rowCount()
        self.table.insertRow(line)
        
        cost = p.quantity*s.purchaseCost
        id = QTableWidgetItem(str(p.id))
        product = QTableWidgetItem(s.product)
        quantity = QTableWidgetItem(str(p.quantity))
        purchaseDate = QTableWidgetItem(p.purchaseDate)
        totalCost = QTableWidgetItem(f"R$ {cost}")
        
        self.table.setItem(line, 0, id)
        self.table.setItem(line, 1, product)
        self.table.setItem(line, 2, quantity)
        self.table.setItem(line, 3, totalCost)
        self.table.setItem(line, 4, purchaseDate)