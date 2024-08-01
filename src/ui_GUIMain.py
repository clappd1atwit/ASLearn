from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import sys
from ui_GUISidebar import MySidebar

app = QApplication(sys.argv)
window = MySidebar()

window.show()
app.exec()