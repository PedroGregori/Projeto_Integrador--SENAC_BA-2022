from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import uic

FILE_UI = "view/employees_management.ui"

class Employees_ui(QWidget):
    def __init__(self) :
        super(Employees_ui, self).__init__()
        uic.loadUi(FILE_UI, self)

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents)