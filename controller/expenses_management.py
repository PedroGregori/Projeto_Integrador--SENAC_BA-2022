from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import uic

FILE_UI = "view/management UIs/expenses_management.ui"

class Expenses_ui(QWidget):
    def __init__(self) :
        super(Expenses_ui, self).__init__()
        uic.loadUi(FILE_UI, self)