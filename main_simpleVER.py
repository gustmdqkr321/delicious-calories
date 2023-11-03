import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

# 로그인 화면을 구현하는 Login 클래스
class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)  # login.ui 파일을 로드
        self.loginbutton.clicked.connect(self.loginfunction)  # 로그인 버튼에 loginfunction 메서드 연결
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)  # 비밀번호 입력란 설정
        self.createaccbutton.clicked.connect(self.gotocreate)  # 계정 생성 버튼에 gotocreate 메서드 연결

    # 로그인 버튼을 클릭하면 실행되는 메서드
    def loginfunction(self):
        email=self.email.text()  # 이메일 입력란의 텍스트 가져오기
        password=self.password.text()  # 비밀번호 입력란의 텍스트 가져오기
        print("Successfully logged in with email: ", email, "and password:", password)  # 정보 출력

    # 계정 생성 버튼을 클릭하면 실행되는 메서드
    def gotocreate(self):
        createacc=CreateAcc()  # CreateAcc 클래스의 인스턴스 생성
        widget.addWidget(createacc)  # 위젯에 CreateAcc 클래스 추가
        widget.setCurrentIndex(widget.currentIndex()+1)  # 인덱스 증가

# 계정 생성 화면을 구현하는 CreateAcc 클래스
class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)  # createacc.ui 파일을 로드
        self.signupbutton.clicked.connect(self.createaccfunction)  # 계정 생성 버튼에 createaccfunction 메서드 연결
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)  # 비밀번호 입력란 설정
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)  # 확인용 비밀번호 입력란 설정

    # 계정 생성 버튼을 클릭하면 실행되는 메서드
    def createaccfunction(self):
        email = self.email.text()  # 이메일 입력란의 텍스트 가져오기
        if self.password.text()==self.confirmpass.text():  # 비밀번호와 확인용 비밀번호가 일치하는지 확인
            password=self.password.text()  # 비밀번호 가져오기
            print("Successfully created acc with email: ", email, "and password: ", password)  # 정보 출력
            login=Login()  # Login 클래스의 인스턴스 생성
            widget.addWidget(login)  # 위젯에 Login 클래스 추가
            widget.setCurrentIndex(widget.currentIndex()+1)  # 인덱스 증가

app=QApplication(sys.argv)  # QApplication 인스턴스 생성
mainwindow=Login()  # Login 클래스의 인스턴스 생성
widget=QtWidgets.QStackedWidget()  # 여러 화면을 관리하는 위젯 생성
widget.addWidget(mainwindow)  # 위젯에 Login 클래스 추가
widget.setFixedWidth(480)  # 위젯의 너비 설정
widget.setFixedHeight(620)  # 위젯의 높이 설정
widget.show()  # 위젯 보이기
app.exec_()  # 이벤트 루프 실행
