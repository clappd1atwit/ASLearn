import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple GUI')
        self.setGeometry(100, 100, 300, 200)

        self.button1 = QPushButton('Tutorials', self)
        self.button2 = QPushButton('Free Mode Practice', self)
        self.button3 = QPushButton('Quiz Yourself!', self)

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    gui = MyGUI()
    gui.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()