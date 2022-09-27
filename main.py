from PyQt5.QtWidgets import QApplication
import sys
import qdarkstyle
from qdarkstyle.light.palette import LightPalette
from controller.main_window import MainWindow 

app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet(palette=LightPalette))
janela = MainWindow()
janela.show()
app.exec() 