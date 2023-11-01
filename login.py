import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("로그인 및 회원가입")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.username_label = QLabel("사용자 이름:")
        self.username_input = QLineEdit()
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)

        self.password_label = QLabel("비밀번호:")
        self.password_input = QLineEdit()
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)

        self.login_button = QPushButton("로그인")
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.signup_button = QPushButton("회원가입")
        self.signup_button.clicked.connect(self.signup)
        self.layout.addWidget(self.signup_button)

        self.central_widget.setLayout(self.layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # 여기에서 로그인 로직을 구현하세요
        # CSV 파일에서 사용자 정보를 확인하고 로그인 여부를 판단하세요
        if self.check_credentials(username, password):
            print("로그인 성공")
        else:
            print("로그인 실패")

    def signup(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # 여기에서 회원가입 로직을 구현하세요
        # 사용자 정보를 CSV 파일에 저장하세요
        self.save_to_csv(username, password)
        print("회원가입 완료")

    def check_credentials(self, username, password):
        # 여기에서 CSV 파일에서 사용자 정보를 확인하고 로그인 여부를 판단하세요
        with open('user_info.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if username == row[0] and password == row[1]:
                    return True
        return False

    def save_to_csv(self, username, password):
        # 사용자 정보를 CSV 파일에 저장하세요
        with open('user_info.csv', 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([username, password])

def main():
    app = QApplication(sys.argv)
    login_app = LoginApp()
    login_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
