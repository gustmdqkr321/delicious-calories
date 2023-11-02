
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from image_upload import ImageUploaderApp

# 밑에 두개로 만들기
# from profile_edit import ProfileEditApp
# from calendar_viewer import CalendarViewerApp

class MainMenuApp(QMainWindow): # 메인 페이지, 로그인 -> 메인 -> 메뉴 선택 순서
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("메인 메뉴")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.image_upload_button = QPushButton("이미지 업로드")
        self.image_upload_button.clicked.connect(self.show_image_uploader)
        layout.addWidget(self.image_upload_button)

        self.profile_edit_button = QPushButton("프로필 수정")
        self.profile_edit_button.clicked.connect(self.show_profile_editor)
        layout.addWidget(self.profile_edit_button)

        self.calendar_viewer_button = QPushButton("캘린더 조회")
        self.calendar_viewer_button.clicked.connect(self.show_calendar_viewer)
        layout.addWidget(self.calendar_viewer_button)

        self.central_widget.setLayout(layout)

    def show_image_uploader(self):
        self.image_uploader = ImageUploaderApp()
        self.image_uploader.show()
    # 밑에 두개에 연동 시키기
    def show_profile_editor(self):
        self.profile_editor = ProfileEditApp() 
        self.profile_editor.show()

    def show_calendar_viewer(self):
        self.calendar_viewer = CalendarViewerApp()
        self.calendar_viewer.show()

if __name__ == '__main__':
    app = MainApp(sys.argv)
    app.login_app.show()
    sys.exit(app.exec_())
