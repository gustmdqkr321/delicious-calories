import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class ProfileEditApp(QMainWindow):
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
        # 여기에서 목표 숫자를 저장하거나 필요한 작업을 수행하세요.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProfileEditApp()
    window.show()
    sys.exit(app.exec_())
