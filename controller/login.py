from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

FILE_UI = "view/login_screen.ui"

class Login_ui(QWidget):
    def __init__(self):
        super(Login_ui, self).__init__()
        uic.loadUi(FILE_UI, self)