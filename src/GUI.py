import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI Landscape for ASLearning")
        self.setGeometry(90, 90, 600, 400)  # Set window size to full screen
        self.setWindowIcon(QIcon("ASLearning pic.PNG"))

        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Set background image (ASLearning)
        background_label = QLabel(self.central_widget)
        pixmap = QPixmap("ASLearning pic.PNG")
        scaled_pixmap = pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio)
        background_label.setPixmap(scaled_pixmap)
        background_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        background_label.resize(self.size())
        background_label.setScaledContents(True)

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

    def show_tutorials_page(self):
        # Replace current widget with Tutorials page
        tutorials_page = QWidget()
        tutorials_page.setStyleSheet("background-color: lightblue;")
        self.setCentralWidget(tutorials_page)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Show window in full screen
    sys.exit(app.exec())
