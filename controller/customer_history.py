from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import uic

FILE_UI = 'view/customer_history.ui'

class customer_history(QWidget):
    def __init__(self):
        super(customer_history, self).__init__()
        uic.loadUi(FILE_UI, self)
        
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents)
        
        self.table2.horizontalHeader().setStretchLastSection(True)
        self.table2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table2.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)