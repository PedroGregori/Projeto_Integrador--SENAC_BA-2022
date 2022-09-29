from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QDate, QTime, Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QStatusBar
from PyQt5 import uic

from controller.home import Home_ui
from controller.sell import Sell_ui
from controller.customer_management import Customer_ui
from controller.users_management import Users_ui
from controller.stock_management import Stock_ui
from controller.expenses_management import Expenses_ui
from controller.sales_management import SalesManagement_ui
#from controller.login import Login_ui
from model.userDAO import User_DAO
from model.user import User

FILE_UI = 'view/main_window.ui'


class MainWindow(QMainWindow):

    managementMenuEnable = False

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(FILE_UI, self)
        
        #self.Login_ui = Login_ui(self)
        self.pageHome = Home_ui()
        self.pageSale = Sell_ui()
        self.pageSale.openCustomerWin.connect(
            lambda: self.stackedWidget.setCurrentIndex(2))
        self.pageCustomer = Customer_ui()
        self.pageUsers = Users_ui()
        self.pageStock = Stock_ui()
        self.pageSales_management = SalesManagement_ui()
        self.pageExpenses = Expenses_ui()

        self.stackedWidget.addWidget(self.pageHome)
        self.stackedWidget.addWidget(self.pageSale)
        self.stackedWidget.addWidget(self.pageCustomer)
        self.stackedWidget.addWidget(self.pageUsers)
        self.stackedWidget.addWidget(self.pageStock)
        self.stackedWidget.addWidget(self.pageExpenses)
        self.stackedWidget.addWidget(self.pageSales_management)

        self.Btn_Home.clicked.connect(self.actionMenu)
        self.Btn_Sale.clicked.connect(self.actionMenu)
        self.Btn_CustomerReg.clicked.connect(self.actionMenu)
        self.Btn_users.clicked.connect(self.actionMenu)
        self.Btn_stock.clicked.connect(self.actionMenu)
        self.Btn_expenses.clicked.connect(self.actionMenu)
        self.Btn_salesManagement.clicked.connect(self.actionMenu)


        self.Btn_Toggle.clicked.connect(
            lambda: self.toggleMenu(170, True))
        self.Btn_Management.clicked.connect(
            lambda: self.managementMenu(124, True))

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def recurring_timer(self):
        now = QDate.currentDate()
        time = QTime.currentTime()
        self.statusBar.showMessage(
            f'{now.toString(Qt.DefaultLocaleLongDate)} - {time.toString()} ')
        
    """def compareUser(self, user):
        userType = []
        for u in user:
            userInfo = User(u.id, u.name, u.cpf, u.rg, u.address, u.salary,
                            u.user, u.password, u.email, u.phone, u.userType)
            userType.append(userInfo.userType)
        print(userType)
        if "Funcionario" in userType:
            self.Btn_management.setEnabled(False)"""

    def actionMenu(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "Btn_Home":
            self.stackedWidget.setCurrentIndex(0)
        if btnName == "Btn_Sale":
            self.stackedWidget.setCurrentIndex(1)
        if btnName == "Btn_CustomerReg":
            self.stackedWidget.setCurrentIndex(2)
        if btnName == "Btn_users":
            self.stackedWidget.setCurrentIndex(3)
        if btnName == "Btn_stock":
            self.stackedWidget.setCurrentIndex(4)
        if btnName == "Btn_expenses":
            self.stackedWidget.setCurrentIndex(5)
        if btnName == "Btn_salesManagement":
            self.stackedWidget.setCurrentIndex(6)

    def toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.frame_dashboard.width()
            maxExtend = maxWidth
            standard = 0

        if width == 0:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        self.animation = QPropertyAnimation(
            self.frame_dashboard, b"minimumWidth")
        self.animation.setDuration(400)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animation.start()

    def managementMenu(self, maxHeight, enable):
        if self.managementMenuEnable:
            self.frame_management.setFixedHeight(0)
        else:
            self.frame_management.setFixedHeight(maxHeight)

        self.managementMenuEnable = not self.managementMenuEnable