import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from image_upload import ImageUploaderApp
from login import LoginApp
# from profile_edit import ProfileEditApp
# from calendar_viewer import CalendarViewerApp 
from main_page import MainMenuApp

class MainApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        # 로그인 앱 인스턴스 생성
        self.login_app = LoginApp()
        self.login_app.login_button.clicked.connect(self.show_main_menu)

    def show_main_menu(self):
        # 로그인 성공 시 메인 메뉴로 전환
        if self.login_app.check_credentials(self.login_app.username_input.text(), self.login_app.password_input.text()):
            self.main_menu = MainMenuApp()
            self.login_app.close()
            self.main_menu.show()
if __name__ == '__main__':
    app = MainApp(sys.argv)
    app.login_app.show()
    sys.exit(app.exec_())