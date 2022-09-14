from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

#from model.homeDAO import Home_dao as h_DAO


FILE_UI = 'view/sale.ui'

class Sale_ui(QWidget):
    def __init__(self):
        super(Sale_ui, self).__init__()
        uic.loadUi(FILE_UI, self)