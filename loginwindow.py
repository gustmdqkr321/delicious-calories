from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.uic import loadUi
import mysql.connector

class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("login.ui", self)
        self.setWindowTitle("Login")
        self.loginButton.clicked.connect(self.login)
        self.createAccButton.clicked.connect(self.goToCreate)

    def login(self):
        email = self.emailLineEdit.text()
        password = self.passwordLineEdit.text()
        # MySQL 연동 및 로그인 정보 확인
        # 이 부분은 아래에 코드로 작성할 것입니다.
        print(f"Successfully logged in with email: {email} and password: {password}")

    def goToCreate(self):
        create_window = CreateAccountWindow()
        create_window.exec_()

class CreateAccountWindow(QDialog):
    def __init__(self):
        super(CreateAccountWindow, self).__init__()
        loadUi("createacc.ui", self)
        self.setWindowTitle("Create Account")
        self.signupButton.clicked.connect(self.createAccount)

    def createAccount(self):
        email = self.emailLineEdit.text()
        password = self.passwordLineEdit.text()
        confirm_password = self.confirmPassLineEdit.text()
        # MySQL 연동 및 회원가입 정보 저장
        # 이 부분은 아래에 코드로 작성할 것입니다.
        print(f"Successfully created account with email: {email} and password: {password}")
