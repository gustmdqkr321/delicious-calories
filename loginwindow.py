import mysql.connector
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QWidget
# from PyQt5.uic import loadUi
from login_ui import Ui_Form as loginUI
from createacc_ui import Ui_Form as createaccUI
import sys

class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = loginUI()
        self.ui.setupUi(self)

        self.setWindowTitle("Login")
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.createAccButton.clicked.connect(self.goToCreate)

    def login(self):
        email = self.ui.email.text()
        password = self.ui.password.text()
        # MySQL 연동 및 로그인 정보 확인
        # 이 부분은 아래에 코드로 작성할 것입니다.
        print(f"Successfully logged in with email: {email} and password: {password}")

    def goToCreate(self):
        create_window = CreateAccountWindow()
        create_window.exec_()

class CreateAccountWindow(QDialog):
    def __init__(self):
        super(CreateAccountWindow, self).__init__()
        self.ui = createaccUI()
        self.ui.setupUi(self)
        
        self.setWindowTitle("Create Account")
        self.ui.signupButton.clicked.connect(self.createAccount)

    def createAccount(self):
        name = self.ui.name.text()
        email = self.ui.email.text()
        password = self.ui.password.text()
        # confirm_password = self.ui.confirmPassLineEdit.text()
        
        # MySQL 연동 및 회원가입 정보 저장
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="yourusername",
                password="yourpassword",
                database="yourdatabase"
            )
            cursor = conn.cursor()
            query = "INSERT INTO users (email, password) VALUES (%s, %s)"
            data = (email, password)
            cursor.execute(query, data)
            conn.commit()
            conn.close()
            print(f"Successfully created account with email: {email} and password: {password}")
        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table:", error)

