from PyQt5.QtWidgets import QApplication
import sys
import qdarkstyle
from qdarkstyle.light.palette import LightPalette
from controller.login import Login_ui

app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet(palette=LightPalette))
login = Login_ui()
login.show()
app.exec()
