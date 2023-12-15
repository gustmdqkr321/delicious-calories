import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
from main_page_ui import Ui_Form as mainUI
from calendar_page import CalendarWindow
from profile_edit import profileEditApp
from image_upload import ImageUploaderApp
from goal_edit import goalEditApp
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainUI()
        self.ui.setupUi(self)
        self.profile_edit = profileEditApp()  # ProfileEditApp 인스턴스 생성
        
        # 이미지 레이블을 생성합니다.
        self.profile_image_label = QLabel(self.ui.profile_image)
        self.profile_image_label.setGeometry(20, 20, 30, 30)  # 적절한 위치와 크기로 조절하세요.
        self.profile_edit.confirm_signal.connect(self.update_profile_image)
        
        self.goal_edit = goalEditApp()  # GoalEditApp 인스턴스 생성
        self.goal_edit.goal_saved_signal.connect(self.update_goal)

        self.goal_label = QLabel(self.ui.goal_content)
        self.goal_label.setGeometry(20, 50, 200, 30)  # 적절한 위치와 크기로 조절하세요.

        self.buttonHandle()

    def update_goal(self, goal):
        print("새로운 목표:", goal)
        self.goal_label.setText(f"현재 목표: {goal}")


    def update_profile_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.profile_image_label.setPixmap(pixmap)

    def buttonHandle(self):
        self.ui.uploadfoodButton.clicked.connect(self.show_image_uploader)
        self.ui.profileEditButton.clicked.connect(self.show_profile_editor)
        self.ui.calenderButton.clicked.connect(self.show_calendar_viewer)
        self.ui.goalEditButton.clicked.connect(self.show_goal_editor)

    def show_image_uploader(self):
        self.image_uploader = ImageUploaderApp()
        self.image_uploader.show()

    def show_profile_editor(self):
        self.profile_edit.confirm_signal.connect(self.update_profile_image)
        self.profile_edit.show()

    def show_calendar_viewer(self):
        self.calendar_viewer = CalendarWindow()
        self.calendar_viewer.show()
    
    def show_goal_editor(self):
        # self.goal_editor = goalEditApp() 
        self.goal_edit.goal_saved_signal.connect(self.update_goal)
        self.goal_edit.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
