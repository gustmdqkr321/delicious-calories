import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from image_upload import ImageUploaderApp
from login import LoginApp

class MainApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        # 로그인 앱 인스턴스 생성
        self.login_app = LoginApp()
        self.login_app.login_button.clicked.connect(self.show_image_uploader)

    def show_image_uploader(self):
        # 로그인 성공 시 이미지 업로더 앱으로 전환
        if self.login_app.check_credentials(self.login_app.username_input.text(), self.login_app.password_input.text()):
            self.image_uploader = ImageUploaderApp()
            self.login_app.close()
            self.image_uploader.show()

if __name__ == '__main__':
    app = MainApp(sys.argv)
    app.login_app.show()
    sys.exit(app.exec_())
