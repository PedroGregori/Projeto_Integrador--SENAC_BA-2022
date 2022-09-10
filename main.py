from PyQt5.QtWidgets import QApplication
import sys
from controller.main_window import MainWindow 

app = QApplication(sys.argv)
app.setStyle('Fusion')                               
janela = MainWindow()
janela.show()
app.exec() 
