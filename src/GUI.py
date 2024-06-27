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
        self.tips_button.clicked.connect(self.show_tips)
        layout.addWidget(self.tips_button)

        self.funfacts_button = QPushButton("What is ASL? Fun Facts")
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

    def show_tips(self):
        self.tips_window = TipsPage()
        self.tips_window.show()
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

        back_button = QPushButton("Back to Login")
        back_button.clicked.connect(self.show_main)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def show_main(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

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
        self.setGeometry(200, 200, 700, 500)

        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)

        #BACKGROUND PICTURE
        self.background_label = QLabel(self)
        self.background_label.setGeometry(400,0,350,250)
        pixmap = QPixmap("all3.jpg")
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
        font2.setPointSize(16)

        label2 = QLabel("Welcome to ASLearning Tool")
        label2.setFont(font2)
        label2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(label2)

        label3 = QLabel("Your Go-To Resource for Mastering ASL")
        label3.setFont(font2)
        label3.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(label3)

        font3 = QFont()
        font3.setPointSize(15)

        quest1 = QLabel("Why ASLearning Tool?")
        quest1.setWordWrap(True)
        #quest1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(quest1)

        quest1.setFont(font3)
        layout.addWidget(quest1)
        self.setLayout(layout)

        ans1 = QLabel('''<p>Our advanced gesture recognition system provides instant feedback on your signs, helping you correct mistakes on the spot and reinforcing accurate learning.
                      We have designed our platform to be easy to use, so you can focus on learning without any technical distractions.
                      Whether you're at home or on the go, ASLearning is available on multiple devices, allowing you to practice and improve your ASL skills whenever it's convenient for you.<\p>''')
        ans1.setWordWrap(True)
        layout.addWidget(ans1)

        quest2 = QLabel("Our Mission")
        quest2.setWordWrap(True)
        #quest1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(quest2)

        quest2.setFont(font3)
        layout.addWidget(quest2)
        self.setLayout(layout)

        ans2 = QLabel('''<p>Our mission is to make ASL accessible and easy to learn for everyone, whether you're a beginner or looking to refine your skills.
                      Our innovative platform leverages cutting-edge technology to provide an enganing and effective learning experience.
                      Using Mediapipe, a powerful tool for real-time hand gesture recognition, we can accurately detect your signs and give immediate feedback. <\p>''')
        ans2.setWordWrap(True)
        layout.addWidget(ans2)

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

class TipsPage(QWidget):
    def __init__(self):
        super().__init__()
        #self.stacked_widget = main_window
        self.setWindowTitle("Tips for ASL")
        self.setGeometry(100, 100, 600, 400)


class ContactPage(QWidget):
    def __init__(self):
        super().__init__()
        #self.stacked_widget = main_window
        self.setWindowTitle("Tips for ASL")
        self.setGeometry(100, 100, 600, 400)

        #BACKGROUND PICTURE
        self.background_label = QLabel(self)
        self.background_label.setGeometry(400,0,350,250)
        pixmap = QPixmap("all3.jpg")
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()  
    sys.exit(app.exec())
