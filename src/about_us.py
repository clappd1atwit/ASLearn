import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QGridLayout, QMessageBox, QStackedWidget, QSizePolicy
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap
#import GUI.LoginWindow

'''
class AboutUsPage(QWidget):
    def __init__(self):
        super().__init__()
        #self.stacked_widget = main_window
        self.setWindowTitle("About Us")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout

        about_label = QLabel("This is the ASLearning website", self)
        about_label.setWordWrap(True)
        layout.addWidget(about_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        back_button = QPushButton("Back to Login")
        back_button.clicked.connect(self.show_login)
        layout.addWidget(back_button)

        #self.setLayout(layout)

    #def show_login(self):
     #   self.login_window.switch_page("login")
        #self.main_window = LoginWindow()
        #self.main_window.show()
        #self.close()
        '''