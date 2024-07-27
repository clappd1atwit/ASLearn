import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QGridLayout, QMessageBox, QStackedWidget, QSizePolicy, QHBoxLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QMovie
from PyQt6.QtGui import QFont
from sandboxGUI_liam import MainWindow as SandboxMainWindow

connection = sqlite3.connect("src/Database/Users.db")
cursor = connection.cursor()

def check_login_credentials(username, password):
    database = sqlite3.connect("src/Database/Users.db")
    cursor = database.cursor()
    # Check if the email and password match in the LOGINS table
    cursor.execute("SELECT COUNT(*) FROM Users WHERE Username=? AND Password=?", (username, password))
    login_count = cursor.fetchone()[0]

    if login_count > 0:
        return True
    else:
        return False
    database.commit()
    database.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100,100,600,400)

        #BACKGROUND PICTURE
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0,0,600,400)
        pixmap = QPixmap("src/images/ASLearning pic.PNG")
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

        container = QWidget(self)
        container.setGeometry(150, 100, 300, 200)
        container.setStyleSheet("background: transparent;")

        layout = QVBoxLayout(container)

        button_style = """
            QPushButton {
                font-weight: bold;
                border: 2px solid white;  /* White border around the button */
                border-radius: 5px;      /* Rounded corners */
                padding: 5px;            /* Space between text and border */
                background-color: rgba(0, 0, 0, 150); /* Semi-transparent background */
                color: white;            /* Text color */
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 100); /* Change on hover */
            }
        """

        self.login_button = QPushButton("Login Account",self)
        self.login_button.setStyleSheet(button_style)
        self.login_button.setGeometry(250,80,100,30)
        self.login_button.clicked.connect(self.show_login)
        layout.addWidget(self.login_button)

        self.about_button = QPushButton("About us",self)
        self.about_button.setStyleSheet(button_style)
        self.about_button.setGeometry(250,130,100,30)
        self.about_button.clicked.connect(self.show_about)
        layout.addWidget(self.about_button)

        self.tips_button = QPushButton("Tips",self)
        self.tips_button.setStyleSheet(button_style)
        self.tips_button.setGeometry(250,180,100,30)
        self.tips_button.clicked.connect(self.show_tips)
        layout.addWidget(self.tips_button)

        self.funfacts_button = QPushButton("What is ASL? Fun Facts",self)
        self.funfacts_button.setStyleSheet(button_style)
        self.funfacts_button.setGeometry(225,230,150,30)
        self.funfacts_button.clicked.connect(self.show_funfacts)
        layout.addWidget(self.funfacts_button)

        self.contact_button = QPushButton("Contact Us",self)
        self.contact_button.setStyleSheet(button_style)
        self.contact_button.setGeometry(250,280,100,30)
        self.contact_button.clicked.connect(self.show_contact)
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

    def show_contact(self):
        self.contact_window = ContactPage()
        self.contact_window.show()
        self.close()

    def show_funfacts(self):
        self.funfacts_window = FunFactsPage()
        self.funfacts_window.show()
        self.close()


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 600, 400)

        # BACKGROUND PICTURE
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 600, 400)
        pixmap = QPixmap("src/images/ASLearning pic.PNG")
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

        self.back_button = QPushButton("Back",self)
        self.back_button.setGeometry(10,10,50,50)
        self.back_button.clicked.connect(self.show_main)

    def show_main(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        DbConnect = sqlite3.connect("src/Database/Users.db")
        db = DbConnect.cursor()

        if check_login_credentials(username, password):
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
        self.setGeometry(0, 0, 700, 500)

        gif_width = 180
        gif_height = 180

        self.label = QLabel(self)
        self.label.setFixedSize(gif_width,gif_height)
        self.movie = QMovie("src/images/about us dan.gif")
        self.movie.setScaledSize(self.label.size())
        self.label.setMovie(self.movie)
        self.movie.start()
        self.setFixedSize(self.movie.frameRect().width()+600, self.movie.frameRect().height()+400)
        self.label.setGeometry(550,300,350,250)


        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)

        #BACKGROUND PICTURE
        self.background_label = QLabel(self)
        self.background_label.setGeometry(400,0,350,250)
        pixmap = QPixmap("src/images/all3_about_us.jpg")
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

        layout = QVBoxLayout()
        self.label = QLabel("ASLearning: About Us",self)

        self.label.setFont(font1)
        layout.addWidget(self.label)
        self.label.setGeometry(50,0,200,200)
        self.setLayout(layout)

        font2 = QFont()
        font2.setPointSize(16)

        self.label2 = QLabel("Welcome to ASLearning Tool",self)
        self.label2.setFont(font2)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.label2)

        self.label3 = QLabel("Your Go-To Resource for Mastering ASL",self)
        self.label3.setFont(font2)
        self.label3.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.label3)

        font3 = QFont()
        font3.setPointSize(15)

        self.quest1 = QLabel("Why ASLearning Tool?",self)
        self.quest1.setWordWrap(True)
        self.quest1.setGeometry(10,200,200,200)
        #quest1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #layout.addWidget(quest1)

        self.quest1.setFont(font3)
        #layout.addWidget(self.quest1)
        self.setLayout(layout)

        self.ans1 = QLabel("Our advanced gesture recognition system provides instant feedback on your signs, helping you correct mistakes on the spot and reinforcing accurate learning. We have designed our platform to be easy to use, so you can focus on learning without any technical distractions. Whether you're at home or on the go, ASLearning is available on multiple devices, allowing you to practice and improve your ASL skills whenever it's convenient for you.", self)
        self.ans1.setWordWrap(True)
        self.ans1.setGeometry(5,150,490,400)
        #layout.addWidget(ans1)

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

        self.back_button = QPushButton("Back",self)
        self.back_button.clicked.connect(self.show_main)

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

        #layout = QVBoxLayout()
        #src/images/you're welcome yas.mov

        gif_width = 170
        gif_height = 170

        self.label = QLabel(self)
        self.label.setFixedSize(gif_width,gif_height)
        self.movie = QMovie("src/images/youre welcome yas.gif")
        self.movie.setScaledSize(self.label.size())
        self.label.setMovie(self.movie)
        self.movie.start()
        self.setFixedSize(self.movie.frameRect().width()+400, self.movie.frameRect().height()+400)

        layout = QVBoxLayout()

        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)

        self.text1 = QLabel("Tips for ASL:",self)
        self.text1.setFont(font1)
        #self.text1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text1.setGeometry(200,0,200,200)
        layout.addWidget(self.text1)

        font2 = QFont()
        font2.setPointSize(10)
        
        self.par1 = QLabel("1. Practice Regularly: Consistent practice helps you remember and improve your signing skills. That includes watching others and learning from native signers by observing and mimicking to improve accuracy and fluency.", self)
        self.par1.setWordWrap(True)
        self.par1.setFont(font2)
        self.par1.setGeometry(0,100,600,200)
        layout.addWidget(self.par1)

        self.par2 = QLabel("2. Relax your Hands: Relaxing your hands means that you’re able to sign at a greater speed, with more clarity, and for longer. Be clear with your form.", self)
        self.par2.setWordWrap(True)
        self.par2.setFont(font2)
        self.par2.setGeometry(0,180,600,200)
        layout.addWidget(self.par2)

        self.par3 = QLabel("3. Focus on Facial Expressions: They are a great and crucial tool to use when it comes to communicationin by conveying tone and emotion in ASL. ", self)
        self.par3.setWordWrap(True)
        self.par3.setFont(font2)
        self.par3.setGeometry(0,250,600,200)
        layout.addWidget(self.par3)

        self.par4 = QLabel("4. Be clear in your form: Keeping your form in check is a considerate way to ensure that your message is completely understood by the end receiver. The dominant hand does most of the signing, while the non-dominant hand supports.", self)
        self.par4.setWordWrap(True)
        self.par4.setFont(font2)
        self.par4.setGeometry(0,320,600,200)
        layout.addWidget(self.par4)

        self.par5 = QLabel("5. Practice on camera: That's why ASLearning is here for! Recording yourself signing on camera is an effective way to pick up on the points of weakness in your technique which you or others may have not noticed otherwise.", self)
        self.par5.setWordWrap(True)
        self.par5.setFont(font2)
        self.par5.setGeometry(0,395,600,200)
        layout.addWidget(self.par5)

        self.back_button = QPushButton("Back",self)
        self.back_button.clicked.connect(self.show_main)

    def show_main(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

class FunFactsPage(QWidget):
    def __init__(self):
        super().__init__()
        #self.stacked_widget = main_window
        self.setWindowTitle("What is ASL? Fun Facts")
        self.setGeometry(100, 100, 600, 350)

        gif_width = 170
        gif_height = 170

        self.label = QLabel(self)
        self.label.setFixedSize(gif_width,gif_height)
        self.movie = QMovie("src/images/what is asl liam.gif")
        self.movie.setScaledSize(self.label.size())
        self.label.setMovie(self.movie)
        self.movie.start()
        self.setFixedSize(self.movie.frameRect().width()+400, self.movie.frameRect().height()+400)
        self.label.setGeometry(400,0,200,200)

        layout = QVBoxLayout()

        #layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignLeft)

        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)

        #BACKGROUND PICTURE
        self.background_label = QLabel(self)
        self.background_label.setGeometry(400,0,350,250)
        pixmap = QPixmap("all3_about_us.jpg")
        self.background_label.setGeometry(0,0,600,350)
        pixmap = QPixmap("wallpaper green.jpg")
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

        layout = QVBoxLayout()
        self.label1 = QLabel("What is ASL?",self)
        self.label1.setFont(font1)
        #self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #layout.addWidget(self.label1)
        self.label1.setGeometry(00,0,200,100)
        #self.setLayout(layout)

        font2 = QFont()
        font2.setPointSize(10)

        self.paragraph1 = QLabel("American Sign Language is a natural language that is expressed by movements of the hands and face with the same linguistic properties as spoken languages. It is the primary language of many North Americans who are deaf and hard of hearing.", self)
        self.paragraph1.setWordWrap(True)
        self.paragraph1.setFont(font2)
        #self.paragraph1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.paragraph1.setGeometry(0,100,400,50)
        #layout.addWidget(self.paragraph1)
        #self.setLayout(layout)

        self.label2 = QLabel("Fun Facts", self)
        self.label2.setFont(font1)
        self.label2.setGeometry(0,100,400,250)
        #layout.addWidget(self.label2)
        #self.setLayout(layout)

        self.label3 = QLabel("1. ASL originated in the early 19th century at the American School for Deaf in Hartford, Connecticut. It was influenced by French Sign Language (LSF).", self)
        self.label3.setFont(font2)
        #layout.addWidget(self.label3)
        #self.setLayout(layout)
        self.label3.setWordWrap(True)
        self.label3.setGeometry(0,150,580,300)

        self.label4 = QLabel("2. ASL has its own grammar, syntax, and vocabulary, making it a distinct and complete language.",self)
        self.label4.setFont(font2)
        #layout.addWidget(self.label4)
        #self.setLayout(layout)
        self.label4.setWordWrap(True)
        self.label4.setGeometry(0,200,580,300)

        self.label5 = QLabel("3. Facial expressions and body language play a crucial role in ASL. They can indicate tone and emotions.",self)
        self.label5.setFont(font2)
        #layout.addWidget(self.label5)
        #self.setLayout(layout)
        self.label5.setWordWrap(True)
        self.label5.setGeometry(0,250,580,300)

        self.label6 = QLabel("4. ASL is the third most common native language in the United States.",self)
        self.label6.setFont(font2)
        #layout.addWidget(self.label6)
        #self.setLayout(layout)
        self.label6.setWordWrap(True)
        self.label6.setGeometry(0,300,580,300)


        self.back_button = QPushButton("Back",self)
        self.back_button.clicked.connect(self.show_main)

    def show_main(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()
        

class ContactPage(QWidget):
    def __init__(self):
        super().__init__()
        #self.stacked_widget = main_window
        self.setWindowTitle("Contact Us - Team Members")
        self.setGeometry(100, 100, 700, 500)

        
        #BACKGROUND PICTURE
        self.pic_label = QLabel(self)
        self.pic_label.setGeometry(0,0,700,500)
        pixmap = QPixmap("src/images/wallpaper yellow.jpg")
        self.pic_label.setPixmap(pixmap)
        self.pic_label.setScaledContents(True)

        #FIRST PICTURE
        self.pic_label1 = QLabel(self)
        self.pic_label1.setGeometry(185,0,325,225)
        pixmap = QPixmap("src/images/all3_contact_us.jpeg")
        self.pic_label1.setPixmap(pixmap)
        self.pic_label1.setScaledContents(True)

        layout = QVBoxLayout()

        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)

        text_label1 = QLabel("Meet the CEOs", self)
        text_label1.setFont(font1)
        text_label1.setGeometry(275, 200, 200, 100)
        self.setLayout(layout)

        font2 = QFont()
        font2.setPointSize(13)

        font3 = QFont()
        font3.setPointSize(10)
        font3.setItalic(True)

        #Dan's contact and picture
        self.pic_label2 = QLabel(self)
        self.pic_label2.setGeometry(50, 300, 125, 125)
        pixmap = QPixmap("src/images/dan_headshot.jpeg")
        self.pic_label2.setPixmap(pixmap)
        self.pic_label2.setScaledContents(True)

        text_label2 = QLabel("Dan Clapp", self)
        text_label2.setFont(font2)
        text_label2.setGeometry(70, 385, 200, 100)
        self.setLayout(layout)

        text_label3 = QLabel("clappd1@wit.edu",self)
        text_label3.setFont(font3)
        text_label3.setGeometry(55, 405, 220, 100)
        self.setLayout(layout)

        '''text_label4 = QLabel("+1 (774) 330-5311",self)
        text_label4.setFont(font3)
        text_label4.setGeometry(50, 420, 220, 100)
        self.setLayout(layout)'''

        #Yass's contact and picture
        self.pic_label3 = QLabel(self)
        self.pic_label3.setGeometry(290, 300, 125, 125)
        pixmap = QPixmap("src/images/yasmina_headshot.jpeg")
        self.pic_label3.setPixmap(pixmap)
        self.pic_label3.setScaledContents(True)

        text_label5 = QLabel("Yasmina Habchi", self)
        text_label5.setFont(font2)
        text_label5.setGeometry(295, 385, 200, 100)
        self.setLayout(layout)

        text_label6 = QLabel("habchiy@wit.edu",self)
        text_label6.setFont(font3)
        text_label6.setGeometry(305, 405, 220, 100)
        self.setLayout(layout)

        '''text_label7 = QLabel("+1 (617) 356-4991",self)
        text_label7.setFont(font3)
        text_label7.setGeometry(300, 420, 220, 100)
        self.setLayout(layout)'''


        #Liam's contact and picture
        self.pic_label4 = QLabel(self)
        self.pic_label4.setGeometry(505, 300, 125, 125)
        pixmap = QPixmap("src/images/liam_headshot.jpeg")
        self.pic_label4.setPixmap(pixmap)
        self.pic_label4.setScaledContents(True)

        text_label8 = QLabel("Liam Nasr", self)
        text_label8.setFont(font2)
        text_label8.setGeometry(530, 385, 200, 100)
        self.setLayout(layout)

        text_label9 = QLabel("nasrl@wit.edu",self)
        text_label9.setFont(font3)
        text_label9.setGeometry(527, 405, 220, 100)
        self.setLayout(layout)

        '''text_label10 = QLabel("+1 (781) 690-0947",self)
        text_label10.setFont(font3)
        text_label10.setGeometry(515, 420, 220, 100)
        self.setLayout(layout)'''

        self.back_button = QPushButton("Back",self)
        self.back_button.setGeometry(10,10,50,50)
        self.back_button.clicked.connect(self.show_main)

    def show_main(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()  
    sys.exit(app.exec())
