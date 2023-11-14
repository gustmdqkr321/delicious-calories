
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from image_upload import ImageUploaderApp
from profile_edit import ProfileEditApp
from main_page_ui import Ui_Form as mainUI
from calendar_page import CalendarWindow

class MainWindow(QMainWindow): # 메인 페이지, 로그인 -> 메인 -> 메뉴 선택 순서
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainUI()
        self.ui.setupUi(self)

        self.buttonHandle()

    def buttonHandle(self):
        self.ui.uploadfoodButton.clicked.connect(self.show_image_uploader)
        
        self.ui.profileEditButton.clicked.connect(self.show_profile_editor)
 
        self.ui.calenderButton.clicked.connect(self.show_calendar_viewer)
        
        self.ui.goalEditButton.clicked.connect(self.show_goal_editor)

    def show_image_uploader(self):
        self.image_uploader = ImageUploaderApp()
        self.image_uploader.show()
    # 밑에 두개에 연동 시키기
    def show_profile_editor(self):
        self.profile_editor = ProfileEditApp() 
        self.profile_editor.show()

    def show_calendar_viewer(self):
        self.calendar_viewer = CalendarWindow()
        self.calendar_viewer.show()
    
    def show_goal_editor(self):
        pass
        #self.goal_editor.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())