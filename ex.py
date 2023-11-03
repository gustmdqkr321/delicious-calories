import sys
from PyQt5.QtWidgets import QApplication, QWidget
from login_ui import Ui_Form

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
