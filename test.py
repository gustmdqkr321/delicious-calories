import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PIL import Image

class ImageUploaderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('이미지 업로더 앱')
        self.setGeometry(100, 100, 800, 600)  # 윈도우 크기를 초기화합니다.

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)  # 이미지를 가운데 정렬합니다.
        self.image_label.setScaledContents(True)

        self.upload_button = QPushButton('이미지 업로드')
        self.upload_button.clicked.connect(self.uploadImage)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.upload_button)

        self.setLayout(layout)

    def uploadImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        filePath, _ = QFileDialog.getOpenFileName(self, '이미지 업로드', '', '이미지 파일 (*.png *.jpg *.jpeg *.bmp *.gif)', options=options)

        if filePath:
            print("파일 경로:", filePath)  # 디버그 출력
            try:
                image = Image.open(filePath)
                max_width, max_height = self.image_label.width(), self.image_label.height()
                image.thumbnail((max_width, max_height))
                pixmap = QPixmap.fromImage(QImage(image.tobytes(), image.width, image.height, image.width * 3, QImage.Format_RGB888))
                self.image_label.setPixmap(pixmap)
            except Exception as e:
                print("이미지를 로드하지 못했습니다:", e)  # 디버그 출력

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageUploaderApp()
    window.show()
    sys.exit(app.exec_())
