from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from model.userDAO import User_DAO
from model.LoginData import Login_Data
from controller.main_window import MainWindow


FILE_UI = "view/login_screen.ui"


class Login_ui(QWidget):
    def __init__(self):
        super(Login_ui, self).__init__()
        uic.loadUi(FILE_UI, self)

        self.Btn_enter.clicked.connect(self.enter)

    def enter(self):
        login = self.login.text()
        password = self.password.text()
        newLogin = Login_Data(login, password)
        user = User_DAO.compareUser(newLogin)
        if len(user) == 0:
            print("usuário incorreto")
        else:
            u = user[0]
            self.hide()
            window = MainWindow(u, Login_ui)
            window.show()
