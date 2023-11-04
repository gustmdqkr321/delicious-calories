import sys
from PyQt5.QtWidgets import QApplication, QDialog
from loginwindow import LoginWindow
from main_page import MainMenuApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    if login_window.exec_() == QDialog.Accepted:  # 로그인이 성공해 로그인창이 정상적으로 닫혔을 경우
        main_menu = MainMenuApp()
        main_menu.show()
        sys.exit(app.exec_())