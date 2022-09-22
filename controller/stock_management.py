from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import uic

FILE_UI = "view/management UIs/stock_management.ui"

class Stock_ui(QWidget):
    def __init__(self) :
        super(Stock_ui, self).__init__()
        uic.loadUi(FILE_UI, self)
