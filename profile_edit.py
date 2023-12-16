import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PIL import Image
from database_utils import db_instance
import os
import shutil

class profileEditApp(QMainWindow):
    confirm_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.initUI()  

    def initUI(self):
        self.setWindowTitle('프로필 수정')
        self.setGeometry(100, 100, 800, 600)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setScaledContents(True)

        self.upload_button = QPushButton('이미지 업로드')
        self.upload_button.clicked.connect(self.uploadImage)

        self.confirm_button = QPushButton('확인')
        self.confirm_button.clicked.connect(self.confirmImage)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.upload_button)
        layout.addWidget(self.confirm_button)

        # 전체 레이아웃 설정
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.image_path = ""  # 업로드된 이미지 경로를 저장할 변수    
    
    def uploadImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        filePath, _ = QFileDialog.getOpenFileName(self, '이미지 업로드', '', '이미지 파일 (*.png *.jpg *.jpeg *.bmp *.gif)', options=options)

        if filePath:
            print("파일 경로:", filePath)
            self.image_path = filePath  # 이미지 경로 저장
            try:
                image = Image.open(filePath)
                max_width, max_height = self.image_label.width(), self.image_label.height()
                image.thumbnail((max_width, max_height))
                pixmap = QPixmap.fromImage(QImage(image.tobytes(), image.width, image.height, image.width * 3, QImage.Format_RGB888))

                # 이미 레이아웃이 설정되어 있으면 제거
                if self.image_label.layout():
                    layout = self.image_label.layout()
                    while layout.count():
                        item = layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.deleteLater()

                self.image_label.setPixmap(pixmap)
            except Exception as e:
                print("이미지를 로드하지 못했습니다:", e)

    def confirmImage(self):
        if self.image_path:
            print("확인 버튼 클릭, 이미지 경로:", self.image_path)
            current_user_id = db_instance.get_user_id()  # 현재 사용자의 ID 가져오기
            if current_user_id:
                # 이미지를 프로필 이미지 폴더에 저장
                profile_image_folder = "profile_image"
                image_filename = f"{current_user_id}.png"  # 파일 이름을 사용자 ID로 저장
                image_path = os.path.join(profile_image_folder, image_filename)

                # 이미지 파일을 프로필 이미지 폴더에 복사
                try:
                    os.makedirs(profile_image_folder, exist_ok=True)
                    shutil.copyfile(self.image_path, image_path)
                except Exception as e:
                    print("이미지를 복사하지 못했습니다:", e)

                # 데이터베이스에 이미지 경로 저장
                db_instance.save_user_profile_image_path(image_path)
                
            # 확인 버튼을 눌렀을 때 원하는 동작 추가
            self.confirm_signal.emit(self.image_path)
            self.close()  # 확인 버튼을 눌렀을 때 창을 닫음
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = profileEditApp()
    window.show()
    sys.exit(app.exec_())
