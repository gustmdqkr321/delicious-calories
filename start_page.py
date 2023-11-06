import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from splash_screen_ui import Ui_SplashScreen

counter = 0

class StartWindow(QMainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))

        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.close()
        counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow()
    sys.exit(app.exec())