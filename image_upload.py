import sys
from PyQt5.QtWidgets import QDateEdit, QComboBox, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt, pyqtSignal, QDate
import pandas as pd
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input, decode_predictions
import numpy as np
from googletrans import Translator
from database_utils import db_instance
import os
class ImageUploaderApp(QWidget):
    calorie_signal = pyqtSignal(float)
    cal_val = 0
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

        self.serving_size_label = QLabel(self)
        self.serving_size_label.setAlignment(Qt.AlignCenter)

        # 식사 시간대 라벨 추가
        self.meal_time_label = QLabel('식사 시간대:', self)

        self.meal_time_combobox = QComboBox(self)
        self.meal_time_combobox.addItem('아침')
        self.meal_time_combobox.addItem('점심')
        self.meal_time_combobox.addItem('저녁')
        # 디폴트로 '아침'을 선택하도록 설정
        self.meal_time_combobox.setCurrentIndex(0)
        
        self.date_edit = QDateEdit(QDate.currentDate())  # 초기 날짜 설정
        self.date_edit.setCalendarPopup(True)  # 달력 팝업 활성화

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.upload_button)

        # 수평 레이아웃 추가
        info_layout = QHBoxLayout()
        info_layout.addWidget(self.result_label)
        info_layout.addWidget(self.calorie_label)
        info_layout.addWidget(self.serving_size_label)
        layout.addLayout(info_layout)

        # 식사 시간대 및 날짜 선택 위젯 추가
        layout.addWidget(self.meal_time_label)
        layout.addWidget(self.meal_time_combobox)
        layout.addWidget(self.date_edit)

        self.save_cal_button = QPushButton("기록 저장")
        self.save_cal_button.clicked.connect(self.save_cal)
        layout.addWidget(self.save_cal_button)

        # 전체 레이아웃 설정
        self.setLayout(layout)

        # 선택한 날짜와 식사 시간대를 저장할 변수 초기화
        self.selected_date = None
        self.selected_meal_time = None

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
            calorie_info, serving_size, serving_unit = self.searchCalorieInfo(translated_label)

            # 결과 텍스트 설정
            result_text = f"이미지는 {food_label}이며, 칼로리는 {calorie_info}kcal입니다."
            self.result_label.setText(result_text)
            self.cal_val = calorie_info
            # 1회 제공량과 단위 표시
            serving_text = f"1회 제공량: {serving_size} {serving_unit}"
            self.serving_size_label.setText(serving_text)

            return food_label
        except Exception as e:
            print("음식을 예측하지 못했습니다:", e)
            return "알 수 없음"

    def searchCalorieInfo(self, food_label):
        try:
            matching_row = self.calorie_data[self.calorie_data['식품명'] == food_label]

            if not matching_row.empty:
                calorie_value = float(matching_row['칼로리'].values[0])
                serving_size = float(matching_row['1회제공량'].values[0])
                serving_unit = matching_row['내용량_단위'].values[0]

                self.calorie_label.setText(f"칼로리: {calorie_value} kcal")
                return calorie_value, serving_size, serving_unit
            else:
                default_calorie_value = "Not Found"
                default_serving_size = "Not Found"
                default_serving_unit = "Not Found"

                self.calorie_label.setText(f"칼로리: {default_calorie_value}")
                self.serving_size_label.setText(f"1회 제공량: {default_serving_size} {default_serving_unit}")

                return default_calorie_value, default_serving_size, default_serving_unit

        except Exception as e:
            print("칼로리 정보를 가져오지 못했습니다:", e)
            return "알 수 없음"

    def translateText(self, text):
        try:
            translated_text = self.translator.translate(text, src='en', dest='ko').text
            return translated_text
        except Exception as e:
            print("텍스트를 번역하지 못했습니다:", e)
            return text
        
    def save_cal(self):
        selected_date = self.date_edit.date().toString(Qt.ISODate)  # 선택한 날짜를 ISO 형식의 문자열로 가져오기
        if selected_date:
            user_id = db_instance.get_user_id()  # 현재 사용자의 아이디 가져오기
            # 식사시간대 저장
            meal_time_index = self.meal_time_combobox.currentIndex()  # 선택한 식사 시간대 인덱스 가져오기
            meal_times = ['아침', '점심', '저녁']  # 각 인덱스에 해당하는 식사 시간대 목록

            meal_time = meal_times[meal_time_index]  # 선택한 인덱스에 해당하는 식사 시간대 가져오기
            print("선택한 식사 시간대:", meal_time)  # 선택한 식사 시간대 출력
            
            # 이미지 이름과 경로 설정
            image_name = f"user_{user_id}_meal_{meal_time}_{selected_date}.jpg"  # 이미지 이름 생성
            image_dir = "food_images"  # 이미지를 저장할 디렉토리
            image_path = os.path.join(image_dir, image_name)  # 이미지 파일 경로 생성
            

            # 이미지 저장
            image_pixmap = self.image_label.pixmap()
            if image_pixmap:
                image_pixmap.save(image_path)
            else:
                print("이미지가 없습니다.")
                return

            calorie = float(self.cal_val)  # 기록된 칼로리를 실수(float)로 변환

            # db_instance의 save_image_data 함수를 호출하여 데이터를 데이터베이스에 저장
            db_instance.save_image_data(user_id, image_name, image_path, meal_time, selected_date, calorie)

            # 목표 저장 신호를 발생시켜 메인 윈도우에 전달
            self.calorie_signal.emit(calorie)  # 실수 값을 보냄
        else:
            print("날짜를 선택하세요.")

        self.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageUploaderApp()
    window.show()
    sys.exit(app.exec_())
