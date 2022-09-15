from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

FILE_UI = 'view/history_window.ui'

class history_window(QWidget):
    def __init__(self):
        super(history_window, self).__init__()
        uic.loadUi(FILE_UI, self)