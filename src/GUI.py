import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QGridLayout, QMessageBox, QStackedWidget, QSizePolicy
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtGui import QFont
from sandboxGUI_liam import MainWindow as SandboxMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100,100,600,400)

        #BACKGROUND PICTURE
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0,0,600,400)
        pixmap = QPixmap("ASLearning pic.PNG")
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

        layout = QVBoxLayout()

        #self.sandbox_gui = MainWindow(self.stacked_widget, self.tutorials_page)

        self.login_button = QPushButton("Login Account")
        self.login_button.setStyleSheet("font-weight: bold;")
        self.login_button.clicked.connect(self.show_login)
        layout.addWidget(self.login_button)

        '''self.username_label = QLabel("Username: ")
        self.username_label.setStyleSheet("font-weight: bold;")
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel("Password: ")
        self.password_label.setStyleSheet("font-weight: bold;")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("font-weight: bold;")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)'''

        self.about_button = QPushButton("About us")
        self.about_button.setStyleSheet("font-weight: bold;")
        self.about_button.clicked.connect(self.show_about)
        layout.addWidget(self.about_button)

        self.tips_button = QPushButton("Tips")
        self.tips_button.setStyleSheet("font-weight: bold;")
        layout.addWidget(self.tips_button)

        self.funfacts_button = QPushButton("Fun Facts")
        self.funfacts_button.setStyleSheet("font-weight: bold;")
        layout.addWidget(self.funfacts_button)

        self.contact_button = QPushButton("Contact Us")
        self.contact_button.setStyleSheet("font-weight: bold;")
        layout.addWidget(self.contact_button)

        self.setLayout(layout)

        container = QWidget(self)
        container.setLayout(layout)
        container.setGeometry(150,100,300,200)
        container.setStyleSheet("background: transparent;")

    def show_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    def show_about(self):
        self.about_window = AboutUsPage()
        self.about_window.show()
        self.close()
'''
    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close() '''

   # def open_about_window(self):
    #    self.about_button = AboutUsPage()
     #   self.about_button.show()
      #  self.close()

'''
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "habchiy" and password == "yasmina":
            print("Login successful")
            self.open_main_window()

        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close() '''

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 600, 400)

        # BACKGROUND PICTURE
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 600, 400)
        pixmap = QPixmap("ASLearning pic.PNG")
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

        layout = QVBoxLayout()

        self.username_label = QLabel("Username: ")
        self.username_label.setStyleSheet("font-weight: bold;")
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel("Password: ")
        self.password_label.setStyleSheet("font-weight: bold;")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("font-weight: bold;")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

        container = QWidget(self)
        container.setLayout(layout)
        container.setGeometry(150, 100, 300, 200)
        container.setStyleSheet("background: transparent;")

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "habchiy" and password == "yasmina":
            print("Login successful")
            self.open_main_window()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

    def open_main_window(self):
        self.main_window = SandboxMainWindow()
        self.main_window.show()
        self.close()

class AboutUsPage(QWidget):
    def __init__(self):
        super().__init__()
        #self.stacked_widget = main_window
        self.setWindowTitle("About Us")
        self.setGeometry(100, 100, 600, 400)

        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)

        #BACKGROUND PICTURE
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0,0,600,400)
        pixmap = QPixmap("ASLearning pic.PNG")
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

        layout = QVBoxLayout()
        label = QLabel("ASLearning: About Us")

        label.setFont(font1)
        layout.addWidget(label)
        self.setLayout(layout)

        label.setFont(font1)
        layout.addWidget(label)

        font2 = QFont()
        font2.setPointSize(15)
        #font2.setItalic(True)

        paragraph = QLabel('''<p>This is the About Us page. <\p>''')
        paragraph.setWordWrap(True)
        paragraph.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(paragraph)

        paragraph.setFont(font2)
        layout.addWidget(paragraph)
        self.setLayout(layout)

        about_label = QLabel("This is the ASLearning website", self)
        about_label.setWordWrap(True)
        layout.addWidget(about_label)

        #container = QWidget(self)
        #container.setLayout(layout)
        #self.setCentralWidget(container)

        back_button = QPushButton("Back to Login")
        back_button.clicked.connect(self.show_main)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def show_main(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()  
    sys.exit(app.exec())
