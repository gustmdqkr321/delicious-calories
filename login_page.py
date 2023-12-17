# login_page.py

import sys
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from login_ui import Ui_Form as loginUI
from createacc_ui import Ui_Form as createaccUI
from main_page import MainWindow
from database_utils import db_instance  # Import db_instance from the database_utils module

class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = loginUI()
        self.ui.setupUi(self)

        self.setWindowTitle("Login")
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.createAccButton.clicked.connect(self.goToCreate)
        
    def login(self):
        userID = self.ui.userID.text()
        password = self.ui.password.text()
        
        # SQLite 연동 및 로그인 정보 확인
        if db_instance.check_login(userID, password):
            QMessageBox.information(self, "Success", "Successfully logged in!")
            # 로그인 성공 시 사용자 아이디 저장
            db_instance.set_user_id(userID)
            self.accept()  # 다이얼로그를 닫고 메인 메뉴 창을 엽니다.
        else:
            QMessageBox.information(self, "Failed", "Login failed. Invalid credentials.")

    def goToCreate(self):
        create_window = CreateAccountWindow()
        create_window.exec_()

    def open_main_menu(self):
        main_menu = MainWindow()
        main_menu.show()
        self.close()

class CreateAccountWindow(QDialog):
    def __init__(self):
        super(CreateAccountWindow, self).__init__()
        self.ui = createaccUI()
        self.ui.setupUi(self)
        
        self.setWindowTitle("Create Account")
        self.ui.signupButton.clicked.connect(self.createAccount)

    def createAccount(self):
        name = self.ui.name.text()
        userID = self.ui.userID.text()
        password = self.ui.password.text()
        
        # SQLite 연동 및 회원가입 정보 저장
        try:
            # Check if userID already exists
            if db_instance.check_user_exist(userID):
                print(f"UserID {userID} already exists. Creation denied.")
                QMessageBox.information(self, "Denied", "UserID already exists. Creation denied.")
            else:
                db_instance.create_user(name, userID, password)
                print(f"Successfully created account with ID: {userID} and password: {password}")
                QMessageBox.information(self, "Success", "Successfully created account!")
                self.close()
        except Exception as e:
            print("Failed to create account:", str(e))
            QMessageBox.information(self, "Failed", "Failed to create account, try again!")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = LoginWindow()
#     sys.exit(app.exec())