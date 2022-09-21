from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import uic

FILE_UI = "view/providers_management.ui"

class Providers_ui(QWidget):
    def __init__(self) :
        super(Providers_ui, self).__init__()
        uic.loadUi(FILE_UI, self)
