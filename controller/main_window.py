import sys
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QStatusBar

from controller.home import Home_ui
from controller.sale import Sale_ui
from controller.customer_management import Customer_ui
from controller.employees_management import Employees_ui
from controller.providers_management import Providers_ui
from controller.stock_management import Stock_ui
from controller.expenses_management import Expenses_ui
from controller.sales_management import SalesManagement_ui


FILE_UI = 'view/main_window.ui'


class MainWindow(QMainWindow):

    managementMenuEnable = False

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(FILE_UI, self)

        self.pageHome = Home_ui()
        self.pageSale = Sale_ui()
        self.pageCustomer = Customer_ui()
        self.pageEmployees = Employees_ui()
        self.pageProviders = Providers_ui()
        self.pageStock = Stock_ui()
        self.pageSales_management = SalesManagement_ui()
        self.pageExpenses = Expenses_ui()

        self.stackedWidget.addWidget(self.pageHome)
        self.stackedWidget.addWidget(self.pageSale)
        self.stackedWidget.addWidget(self.pageCustomer)
        self.stackedWidget.addWidget(self.pageEmployees)
        self.stackedWidget.addWidget(self.pageProviders)
        self.stackedWidget.addWidget(self.pageStock)
        self.stackedWidget.addWidget(self.pageExpenses)
        self.stackedWidget.addWidget(self.pageSales_management)
        

        self.Btn_Home.clicked.connect(self.actionMenu)
        self.Btn_Sale.clicked.connect(self.actionMenu)
        self.Btn_CustomerReg.clicked.connect(self.actionMenu)
        self.Btn_employees.clicked.connect(self.actionMenu)
        self.Btn_providers.clicked.connect(self.actionMenu)
        self.Btn_stock.clicked.connect(self.actionMenu)
        self.Btn_expenses.clicked.connect(self.actionMenu)
        self.Btn_salesManagement.clicked.connect(self.actionMenu)

        self.Btn_Toggle.clicked.connect(
            lambda: self.toggleMenu(150, True))
        self.Btn_Management.clicked.connect(
            lambda: self.managementMenu(141, True))

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def recurring_timer(self):

        now = QDate.currentDate()

        # print(now.toString(Qt.ISODate))
        # print(now.toString(Qt.DefaultLocaleLongDate))

        datetime = QDateTime.currentDateTime()

        # print(datetime.toString())

        time = QTime.currentTime()

        # print(time.toString(Qt.DefaultLocaleLongDate))

        self.statusBar.showMessage(
            f'{now.toString(Qt.DefaultLocaleLongDate)} - {time.toString()} ')

    def actionMenu(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "Btn_Home":
            self.stackedWidget.setCurrentIndex(0)
        if btnName == "Btn_Sale":
            self.stackedWidget.setCurrentIndex(1)
        if btnName == "Btn_CustomerReg":
            self.stackedWidget.setCurrentIndex(2)
        if btnName == "Btn_employees":
            self.stackedWidget.setCurrentIndex(3)
        if btnName == "Btn_providers":
            self.stackedWidget.setCurrentIndex(4)
        if btnName == "Btn_stock":
            self.stackedWidget.setCurrentIndex(5)
        if btnName == "Btn_expenses":
            self.stackedWidget.setCurrentIndex(6)
        if btnName == "Btn_salesManagement":
            self.stackedWidget.setCurrentIndex(7)
            

    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.frame_dashboard.width()
            maxExtend = maxWidth
            standard = 0

            # SET MAX WIDTH
        if width == 0:
            widthExtended = maxExtend
        else:
            widthExtended = standard

            # ANIMATION
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

        """if enable:
            # GET WIDTH
            height = self.frame_management.height()
            maxExtend = maxHeight
            standard = 0

            # SET MAX WIDTH
        if height == 0:
            heightExtended = maxExtend
        else:
            heightExtended = standard
        
        self.animation = QPropertyAnimation(
            self.frame_management, b"minimumHeight")
        self.animation.setDuration(400)
        self.animation.setStartValue(height)
        self.animation.setEndValue(heightExtended)
        self.animation.setEasingCurve(QEasingCurve.Type.Linear)
        self.animation.start()"""
