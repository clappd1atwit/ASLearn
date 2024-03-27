import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple GUI')
        self.setGeometry(100, 100, 300, 200)

        self.button1 = QPushButton('Button 1', self)
        self.button2 = QPushButton('Button 2', self)
        self.button3 = QPushButton('Button 3', self)

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