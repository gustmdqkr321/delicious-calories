import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import pandas as pd
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input, decode_predictions
import numpy as np
from googletrans import Translator

class ImageUploaderApp(QWidget):
    def __init__(self):
        super().__init__()

        # InceptionResNetV2 모델 로드 (Food101 데이터셋 기반)
        self.model = InceptionResNetV2(weights='imagenet')
        self.translator = Translator()
        self.calorie_data = pd.read_csv('test.csv')

        self.initUI()   

    def initUI(self):
        self.setWindowTitle('음식 이미지 업로더 앱')
        self.setGeometry(100, 100, 800, 600)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setScaledContents(True)

        self.upload_button = QPushButton('이미지 업로드')
        self.upload_button.clicked.connect(self.uploadImage)

        self.result_label = QLabel(self)
        self.result_label.setAlignment(Qt.AlignCenter)

        self.calorie_label = QLabel(self)
        self.calorie_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.upload_button)

        # 수평 레이아웃 추가
        info_layout = QHBoxLayout()
        info_layout.addWidget(self.result_label)
        info_layout.addWidget(self.calorie_label)

        # 전체 레이아웃 설정
        layout.addLayout(info_layout)
        self.setLayout(layout)

    def uploadImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        filePath, _ = QFileDialog.getOpenFileName(self, '이미지 업로드', '', '이미지 파일 (*.png *.jpg *.jpeg *.bmp *.gif)', options=options)

        if filePath:
            print("파일 경로:", filePath)
            try:
                image = Image.open(filePath)
                max_width, max_height = self.image_label.width(), self.image_label.height()
                image.thumbnail((max_width, max_height))
                pixmap = QPixmap.fromImage(QImage(image.tobytes(), image.width, image.height, image.width * 3, QImage.Format_RGB888))
                self.image_label.setPixmap(pixmap)

                # 음식 예측 수행
                food_label = self.predictFood(filePath)

                # 음식 라벨을 번역
                translated_label = self.translateText(food_label)
                self.result_label.setText(f"사진은 {translated_label}입니다.")
            except Exception as e:
                print("이미지를 로드하지 못했습니다:", e)

    def predictFood(self, image_path):
        try:
            # 이미지를 모델에 입력할 형식으로 변환
            img = Image.open(image_path).resize((299, 299))
            img_array = keras_image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)

            # 모델에 이미지 입력 및 예측
            predictions = self.model.predict(img_array)

            # 예측 결과 디코딩
            decoded_predictions = decode_predictions(predictions, top=1)[0]
            food_label = decoded_predictions[0][1]
            # 번역하기
            translated_label = self.translateText(food_label)

            # 검색을 통해 음식의 칼로리 얻기
            calorie_info = self.searchCalorieInfo(translated_label)

            # 결과 텍스트 설정
            result_text = f"이미지는 {food_label}이며, 칼로리는 {calorie_info}kcal입니다."
            self.result_label.setText(result_text)

            return food_label
        except Exception as e:
            print("음식을 예측하지 못했습니다:", e)
            return "알 수 없음"

    def searchCalorieInfo(self, food_label):
        try:
            # Search for the food label in the DataFrame
            matching_row = self.calorie_data[self.calorie_data['식품명'] == food_label]

            if not matching_row.empty:
                # If a matching row is found, get the calorie value
                calorie_value = float(matching_row['칼로리'].values[0])
                self.calorie_label.setText(f"칼로리: {calorie_value} kcal")
                return calorie_value
            else:
                # If no matching row is found, set a default value
                default_calorie_value = "Not Found"
                self.calorie_label.setText(f"칼로리: {default_calorie_value}")
                return default_calorie_value

        except Exception as e:
            print("칼로리 정보를 가져오지 못했습니다:", e)
            return "알 수 없음"

    def translateText(self, text):
        try:
            # 음식 라벨을 한국어로 번역
            translated_text = self.translator.translate(text, src='en', dest='ko').text
            return translated_text
        except Exception as e:
            print("텍스트를 번역하지 못했습니다:", e)
            return text

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageUploaderApp()
    window.show()
    sys.exit(app.exec_())
