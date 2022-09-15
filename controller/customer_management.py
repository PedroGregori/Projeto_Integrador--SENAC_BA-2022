from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from controller.history_window import history_window

FILE_UI = 'view/customers_management.ui'

class Customer_ui(QWidget):
    def __init__(self):
        super(Customer_ui, self).__init__()
        uic.loadUi(FILE_UI, self)
        
        self.Btn_History.clicked.connect(self.openHistory)
        self.winistory = None #Variável para guardar a referêncida da janela
        
    def openHistory(self):
        self.winHistory = history_window()
        self.winHistory.show()