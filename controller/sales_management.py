from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import uic

FILE_UI = "view/management UIs/sales_management.ui"

class SalesManagement_ui(QWidget):
    def __init__(self) :
        super(SalesManagement_ui, self).__init__()
        uic.loadUi(FILE_UI, self)
