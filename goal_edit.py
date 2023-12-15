import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt, pyqtSignal

class goalEditApp(QMainWindow):
    goal_saved_signal = pyqtSignal(str)  # 목표 저장 신호

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("프로필 수정")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.goal_label = QLabel("목표 숫자:")
        self.goal_input = QLineEdit()

        self.layout.addWidget(self.goal_label)
        self.layout.addWidget(self.goal_input)

        self.save_goal_button = QPushButton("목표 저장")
        self.save_goal_button.clicked.connect(self.save_goal)
        self.layout.addWidget(self.save_goal_button)

        self.central_widget.setLayout(self.layout)

    def save_goal(self):
        goal = self.goal_input.text()
        self.goal_saved_signal.emit(goal)  # 목표 저장 신호를 발생시켜 메인 윈도우에 전달
        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = goalEditApp()
    window.show()
    sys.exit(app.exec_())
