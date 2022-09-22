from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import uic

FILE_UI = "view/management UIs/providers_management.ui"

class Providers_ui(QWidget):
    def __init__(self) :
        super(Providers_ui, self).__init__()
        uic.loadUi(FILE_UI, self)
        
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents)
