import sys
from PyQt5.QtWidgets import QApplication, QDialog
from start_page import StartWindow
from loginwindow import LoginWindow
from main_page import MainMenuApp

import subprocess
start_path = "start_page.py"
if __name__ == "__main__":
    subprocess.run(["python", start_path]) # 로딩 화면
    
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    
    if login_window.exec_() == QDialog.Accepted:  # 로그인이 성공해 로그인창이 정상적으로 닫혔을 경우
        main_menu = MainMenuApp()
        main_menu.show()
        sys.exit(app.exec_())
        
