import sys
from PyQt5.QtWidgets import QApplication
from loginwindow import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    sys.exit(app.exec_())
