from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import uic
from model.stock import Stock
from model.stockDAO import Stock_DAO

FILE_UI = "view/management UIs/stock_management.ui"

class Stock_ui(QWidget):
    def __init__(self) :
        super(Stock_ui, self).__init__()
        uic.loadUi(FILE_UI, self)
        
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents)
        
        self.Btn_add.clicked.connect(self.add)
        self.Btn_edit.clicked.connect(self.edit)
        self.Btn_delete.clicked.connect(self.delete)
        self.Btn_buy.clicked.connect(self.buy)
        self.Btn_history.clicked.connect(self.openHistory)

    def add(self):
        pass
    
    def edit(self):
        pass
    
    def delete(self):
        pass
    
    def buy(self):
        pass
    
    def openHistory(self):
        pass
    
    def addTableItem(self, s: Stock):
        pass
    
    def updateTable(self, s: Stock):
        pass