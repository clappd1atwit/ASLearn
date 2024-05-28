import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QGridLayout, QMessageBox, QStackedWidget, QSizePolicy
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap
from sandboxGUI_liam import MainWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100,100,600,400)

        #BACKGROUND PICTURE
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0,0,600,400)
        pixmap = QPixmap("ASLearning pic.PNG")
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

        layout = QVBoxLayout()

        #self.sandbox_gui = MainWindow(self.stacked_widget, self.tutorials_page)

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
        container.setGeometry(150,100,300,200)
        container.setStyleSheet("background: transparent;")

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Replace the condition with your actual authentication logic
        if username == "habchiy" and password == "yasmina":
            print("Login successful")
            self.open_main_window()
            #self.parent().show_home_page()
            #self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #self.setWindowTitle("GUI Landscape for ASLearning")
        #self.setGeometry(90, 90, 600, 400)  # the window size is set to full screen
        #self.setWindowIcon(QIcon("ASLearning pic.PNG"))

        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.stacked_widget = QStackedWidget(self.central_widget)
        self.layout.addWidget(self.stacked_widget)


        self.login_window = LoginWindow(self)
        self.stacked_widget.addWidget(self.login_window)

        self.create_home_page()
        self.create_tutorials_page()
        self.create_quiz_page()

        # Set background image (ASLearning)
        #background_label = QLabel(self.central_widget)
        #pixmap = QPixmap("ASLearning pic.PNG")
        #scaled_pixmap = pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio)
        #background_label.setPixmap(scaled_pixmap)
        #background_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #background_label.resize(self.size())
        #background_label.setScaledContents(True)

        # Home page buttons
        self.tutorials_button = QPushButton("Tutorials")
        self.free_mode_button = QPushButton("Free Mode Practice")
        self.quiz_button = QPushButton("Quiz")

        # Connect buttons to respective functions
        self.tutorials_button.clicked.connect(self.show_tutorials_page)
        self.free_mode_button.clicked.connect(self.show_free_mode_page)
        self.quiz_button.clicked.connect(self.show_quiz_page)

        # Add buttons to layout
        self.layout.addWidget(self.tutorials_button)
        self.layout.addWidget(self.free_mode_button)
        self.layout.addWidget(self.quiz_button)

    def create_home_page(self):
        self.home_page = QWidget()
        layout = QVBoxLayout(self.home_page)
        
        background_label = QLabel(self.home_page)
        pixmap = QPixmap("ASLearning pic.PNG")
        scaled_pixmap = pixmap.scaled(QSize(800, 600), Qt.AspectRatioMode.KeepAspectRatio)
        background_label.setPixmap(scaled_pixmap)
        background_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(background_label)

        self.tutorials_button = QPushButton("Tutorials")
        self.free_mode_button = QPushButton("Free Mode Practice")
        self.quiz_button = QPushButton("Quiz")

        self.tutorials_button.clicked.connect(self.show_tutorials_page)
        self.free_mode_button.clicked.connect(self.run_free_mode)
        self.quiz_button.clicked.connect(self.show_quiz_page)

        layout.addWidget(self.tutorials_button)
        layout.addWidget(self.free_mode_button)
        layout.addWidget(self.quiz_button)

        self.stacked_widget.addWidget(self.home_page)

    def create_tutorials_page(self):
        self.tutorials_page = QWidget()
        self.tutorials_layout = QGridLayout(self.tutorials_page)

        # Add buttons A-Z to the tutorials page
        button_size = QSize(50, 50)  # Define the button size for A-Z buttons
        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            button = QPushButton(letter)
            button.setFixedSize(button_size)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            row = i // 6  # 6 buttons per row
            col = i % 6   # column index
            self.tutorials_layout.addWidget(button, row, col)

        self.tutorials_page.setStyleSheet("background-color: lightblue;")
        self.stacked_widget.addWidget(self.tutorials_page)

    def create_quiz_page(self):
        self.quiz_page = QWidget()
        self.quiz_page.setStyleSheet("background-color: lightcoral;")
        self.stacked_widget.addWidget(self.quiz_page)


    def show_quiz_page(self):
        self.stacked_widget.setCurrentWidget(self.quiz_page)

    def show_login_page(self):
        main_window = QWidget()
        self.setCentralWidget(main_window)

    #def show_tutorials_page(self):
        # Replace current widget with Tutorials page
     #   tutorials_page = QWidget()
      #  tutorials_page.setStyleSheet("background-color: lightblue;")
       # self.setCentralWidget(tutorials_page)

    def show_free_mode_page(self):
        # Replace current widget with Free Mode Practice page
        free_mode_page = QWidget()
        free_mode_page.setStyleSheet("background-color: lightgreen;")
        self.setCentralWidget(free_mode_page)

    def show_quiz_page(self):
        # Replace current widget with Quiz page
        quiz_page = QWidget()
        quiz_page.setStyleSheet("background-color: lightcoral;")
        self.setCentralWidget(quiz_page)

    def run_free_mode(self):
        print("Free Mode")
        '''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()  
    sys.exit(app.exec())
