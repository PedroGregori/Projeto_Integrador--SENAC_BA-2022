import sys
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

FILE_UI = 'view/main_window.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(FILE_UI, self)   

        self.Btn_Toggle.clicked.connect(
            lambda: self.toggleMenu(150, True))
        self.Btn_Management.clicked.connect(
            lambda: self.managementMenu(141, True))
        
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
        if enable:
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
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animation.start()