# main_page.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
import re
from main_page_ui import Ui_Form as mainUI
from calendar_page import CalendarWindow
from profile_edit import profileEditApp
from image_upload import ImageUploaderApp
from goal_edit import goalEditApp
from database_utils import db_instance

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainUI()
        self.ui.setupUi(self)

        self.conn = db_instance.get_connection()
        
        self.profile_edit = profileEditApp()
        self.profile_edit.confirm_signal.connect(self.update_profile_image)

        self.goal_edit = goalEditApp()
        self.goal_edit.goal_saved_signal.connect(self.update_goal)

        self.image_upload = ImageUploaderApp()

        self.init_ui()

    def init_ui(self):
        self.button_handle()

        user_name = db_instance.get_user_name()
        self.ui.name.setText(user_name)

        self.profile_image_label = QLabel(self.ui.profile_image)
        self.profile_image_label.setGeometry(20, 20, 100, 100)
        
        # self.goal_label = QLabel(self.ui.goal_content)
        # self.goal_label.setGeometry(20, 50, 200, 30)

        # self.cal_label = QLabel(self.ui.goal_content)
        # self.cal_label.setGeometry(20, 80, 200, 30)
        
        # self.diff_goal_cal_label = QLabel(self.ui.goal_content)
        # self.diff_goal_cal_label.setGeometry(20, 110, 200, 30)

        self.update_profile_image()
        self.update_goal()
    
    def update_profile_image(self, user_image_path=None):
        default_image_path="profile_image/default.jpeg"
        user_image_path = db_instance.get_user_profile_image_path()  # 사용자 프로필 이미지 경로 가져오기
        if not user_image_path:
            user_image_path = default_image_path

        user_pixmap = QPixmap(user_image_path)
        pixmap = user_pixmap.scaled(100, 100, Qt.KeepAspectRatio)
        self.profile_image_label.setPixmap(pixmap)

        layout = QVBoxLayout()
        layout.addWidget(self.profile_image_label)
        layout.setAlignment(Qt.AlignCenter)
        self.ui.profile_image.setLayout(layout)


    def get_user_profile_image_path(self):
        current_user_id = db_instance.get_user_id()
        cursor = self.conn.cursor()
        cursor.execute("SELECT profile_image_path FROM users WHERE id = ?", (current_user_id,))
        result = cursor.fetchone()
        return result[0] if result else None

    def update_goal(self, goal=None):
        if goal is not None:
            db_instance.set_goal(goal)  # 목표를 데이터베이스에 저장
        updated_goal = db_instance.get_goal()  # 데이터베이스에서 최신 목표 칼로리 가져오기
        self.ui.current_goal.setText(f"{updated_goal}")

    def button_handle(self):
        self.ui.uploadfoodButton.clicked.connect(self.show_image_uploader)
        self.ui.profileEditButton.clicked.connect(self.show_profile_editor)
        self.ui.calenderButton.clicked.connect(self.show_calendar_viewer)
        self.ui.goalEditButton.clicked.connect(self.show_goal_editor)

    def show_image_uploader(self):
        self.image_upload.show()

    def show_profile_editor(self):
        self.profile_edit.show()

    def show_calendar_viewer(self):
        self.calendar_viewer = CalendarWindow()
        self.calendar_viewer.show()

    def show_goal_editor(self):
        self.goal_edit.show()

# 테스트용
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
