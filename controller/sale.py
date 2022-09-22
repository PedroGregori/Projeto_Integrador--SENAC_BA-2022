from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic


FILE_UI = 'view/sale.ui'


class Sale_ui(QWidget):
    
    openCustomerWin = pyqtSignal()
    
    def __init__(self):
        super(Sale_ui, self).__init__()
        uic.loadUi(FILE_UI, self)
        
        self.Btn_newCustomer.clicked.connect(lambda: self.openCustomerWin.emit())
