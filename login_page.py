# login_page.py
import sqlite3
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from login_ui import Ui_Form as loginUI
from createacc_ui import Ui_Form as createaccUI
from main_page import MainWindow
# from database_utils import DatabaseUtils
from database_utils import db_instance
import sys

class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = loginUI()
        self.ui.setupUi(self)

        self.setWindowTitle("Login")
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.createAccButton.clicked.connect(self.goToCreate)
        
        self.conn = db_instance.get_connection()
    def login(self):
        userID = self.ui.userID.text()
        password = self.ui.password.text()
        # SQLite 연동 및 로그인 정보 확인
        try:
            # 데이터베이스 연결 가져오기
            conn = db_instance.get_connection()
            cursor = conn.cursor()
            
            # Check if userID and password are valid
            query = "SELECT * FROM users WHERE ID = ? AND password = ?"
            data = (userID, password)
            cursor.execute(query, data)
            result = cursor.fetchone()
            
            if result:
                print(f"Successfully logged in with ID: {userID} and password: {password}")
                QMessageBox.information(self, "Success", "Successfully logged in!")
                # 로그인 성공 시 사용자 아이디 저장
                db_instance.set_user_id(userID)
                
                self.accept()  # 다이얼로그를 닫고 메인 메뉴 창을 엽니다.
            else:
                print("Login failed. Invalid credentials.")
                QMessageBox.information(self, "Failed", "Login failed. Invalid credentials.")

        except sqlite3.Error as error:
            print("Failed to connect to SQLite database:", error)
            QMessageBox.information(self, "Error", "Failed to connect to SQLite database.")


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
            conn = self.sqlite_connection()  # SQLite 연결
            cursor = conn.cursor()
                
            # Check if userID already exists
            check_query = "SELECT * FROM users WHERE ID = ?"
            check_data = (userID,)
            cursor.execute(check_query, check_data)
            result = cursor.fetchone()
            
            if result:
                print(f"UserID {userID} already exists. Creation denied.")
                QMessageBox.information(self, "Denied", "UserID already exists. Creation denied.")
            else:
                query = "INSERT INTO users (username, ID, password) VALUES (?, ?, ?)"
                data = (name, userID, password)
                cursor.execute(query, data)
                conn.commit()
                conn.close()
                print(f"Successfully created account with ID: {userID} and password: {password}")
                QMessageBox.information(self, "Success", "Successfully created account!")
        except sqlite3.Error as error:
            print("Failed to insert record into SQLite table:", error)
            QMessageBox.information(self, "Failed", "Failed to create account, try again!")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = LoginWindow()
#     sys.exit(app.exec())