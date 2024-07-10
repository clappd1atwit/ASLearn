import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QStackedWidget, QSizePolicy, QGridLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI Landscape for ASLearning")
        self.setGeometry(100, 100, 800, 600)  # Set window size to 800x600
        self.setWindowIcon(QIcon("src/images/ASLearning pic.PNG"))

        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create a stacked widget for page navigation
        self.stacked_widget = QStackedWidget(self.central_widget)
        self.layout.addWidget(self.stacked_widget)

        # Create Home page with background image
        self.home_page = QWidget()
        self.home_layout = QVBoxLayout(self.home_page)
        
        background_label = QLabel(self.home_page)
        pixmap = QPixmap("src/images/ASLearning pic.PNG")
        scaled_pixmap = pixmap.scaled(QSize(800, 600), Qt.AspectRatioMode.KeepAspectRatio)
        background_label.setPixmap(scaled_pixmap)
        background_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add buttons to Home page
        self.tutorials_button = QPushButton("Tutorials")
        self.free_mode_button = QPushButton("Free Mode Practice")
        self.quiz_button = QPushButton("Quiz")

        # Connect buttons to respective functions
        self.tutorials_button.clicked.connect(self.show_tutorials_page)
        self.free_mode_button.clicked.connect(self.run_free_mode)
        self.quiz_button.clicked.connect(self.show_quiz_page)

        self.home_layout.addWidget(background_label)
        self.home_layout.addWidget(self.tutorials_button)
        self.home_layout.addWidget(self.free_mode_button)
        self.home_layout.addWidget(self.quiz_button)
        
        self.stacked_widget.addWidget(self.home_page)

        # Create placeholders for other pages
        self.create_tutorials_page()
        self.create_free_mode_page()
        self.create_quiz_page()

    def create_back_button(self, page):
        back_button = QPushButton("Back")
        back_button.setFixedSize(QSize(80, 40))
        back_button.clicked.connect(self.show_home_page)
        layout = QHBoxLayout()
        layout.addStretch()
        layout.addWidget(back_button)
        page_layout = QVBoxLayout(page)
        page_layout.addLayout(layout)
        return page_layout

    def create_tutorials_page(self):
        self.tutorials_page = QWidget()
        tutorials_layout = self.create_back_button(self.tutorials_page)
        grid_layout = QGridLayout()
        
        # Add buttons A-Z to the tutorials page
        button_size = QSize(50, 50)  # Define the button size for A-Z buttons
        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            button = QPushButton(letter)
            button.setFixedSize(button_size)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            button.clicked.connect(lambda _, letter=letter: self.run_module(letter))
            row = i // 6  # 6 buttons per row
            col = i % 6   # column index
            grid_layout.addWidget(button, row, col)
        
        tutorials_layout.addLayout(grid_layout)
        self.tutorials_page.setStyleSheet("background-color: lightblue;")
        self.stacked_widget.addWidget(self.tutorials_page)
    
    def create_free_mode_page(self):
        self.free_mode_page = QWidget()
        self.create_back_button(self.free_mode_page)
        self.free_mode_page.setStyleSheet("background-color: lightgreen;")
        self.stacked_widget.addWidget(self.free_mode_page)
    
    def create_quiz_page(self):
        self.quiz_page = QWidget()
        self.create_back_button(self.quiz_page)
        self.quiz_page.setStyleSheet("background-color: lightcoral;")
        self.stacked_widget.addWidget(self.quiz_page)

    def show_home_page(self):
        self.stacked_widget.setCurrentWidget(self.home_page)

    def show_tutorials_page(self):
        self.stacked_widget.setCurrentWidget(self.tutorials_page)
    
    def run_free_mode(self):
        subprocess.Popen([sys.executable, r"src/handtracking.py"])

    def show_quiz_page(self):
        self.stacked_widget.setCurrentWidget(self.quiz_page)

    def run_module(self, letter):
        subprocess.Popen([sys.executable, r"src/learn_modules.py", letter.lower()])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  
    sys.exit(app.exec())
