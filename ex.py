import sys
from PyQt5.QtWidgets import QApplication, QWidget
from login_ui import Ui_Form

# 이미지 리소스 오류 때문에 ui.py를 가져와서 GUI열기
class LoginForm(QWidget):
    def __init__(self):
        super(LoginForm, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()  # GUI를 화면에 표시합니다.
    sys.exit(app.exec_())
