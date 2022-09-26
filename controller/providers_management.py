from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import uic
from model.provider import Provider
from model.providerDAO import Provider_DAO

FILE_UI = "view/management UIs/providers_management.ui"

class Providers_ui(QWidget):
    def __init__(self) :
        super(Providers_ui, self).__init__()
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
    
    def addTableItem(self, p: Provider):
        pass
    
    def updateTable(self, p: Provider):
        pass