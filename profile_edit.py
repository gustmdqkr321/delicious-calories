import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PIL import Image

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
                self.image_label.setPixmap(pixmap)

            except Exception as e:
                print("이미지를 로드하지 못했습니다:", e)

    def confirmImage(self):
        if self.image_path:
            print("확인 버튼 클릭, 이미지 경로:", self.image_path)
            # 여기에 확인 버튼을 눌렀을 때 원하는 동작 추가
            self.confirm_signal.emit(self.image_path)
            self.close()  # 확인 버튼을 눌렀을 때 창을 닫음
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = profileEditApp()
    window.show()
    sys.exit(app.exec_())
