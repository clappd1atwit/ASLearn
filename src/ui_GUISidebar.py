import typing
from PyQt6 import QtCore
from ui_GUIMenu import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class MySidebar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ASLearning")

        self.Icon_name.setHidden(True)

        self..clicked.connect(self.switch_to_modesPage)
        self.ModeC.clicked.connect(self.switch_to_modesPage)

        self.CaliO.clicked.connect(self.switch_to_CaliPage)
        self.CaliC.clicked.connect(self.switch_to_CaliPage)

        self.ContactO.clicked.connect(self.switch_to_ContactPage)
        self.ContactC.clicked.connect(self.switch_to_ContactPage)

        self.TipsO.clicked.connect(self.switch_to_TipsPage)
        self.TipsC.clicked.connect(self.switch_to_TipsPage)

    def switch_to_modesPage(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_CaliPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_ContactPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_TipsPage(self):
        self.stackedWidget.setCurrentIndex(3)