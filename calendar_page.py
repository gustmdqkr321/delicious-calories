
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
from image_upload import ImageUploaderApp
from database_utils import db_instance

class CalendarWindow(QWidget):
    def __init__(self):
        super(CalendarWindow, self).__init__()
        loadUi("calendarView.ui", self)
        
        self.image_upload = ImageUploaderApp()
        
        # handle buttons
        self.uploadButton.clicked.connect(self.show_image_uploader)
        self.deleteButton.clicked.connect(self.delete_images)
        self.updateButton.clicked.connect(self.updateScreen)
        
        # 시작 시 아침 이미지 표시
        self.updateScreen()
        
    def updateScreen(self):
        selected_date = self.calendarWidget.selectedDate().toPyDate()
        self.display_meal_image(selected_date, "아침", self.breakfast_img)
        self.display_meal_image(selected_date, "점심", self.lunch_img)
        self.display_meal_image(selected_date, "저녁", self.dinner_img)
        self.calculate_goal_rate(selected_date)

    def calculate_goal_rate(self, selected_date):
        try:
            # 사용자의 목표 칼로리 가져오기
            goal_calories = db_instance.get_goal()
            total_calories = 0
            daily_calories_text = ""  # 아침, 점심, 저녁의 칼로리를 담을 텍스트 변수

            # 아침, 점심, 저녁 각각의 칼로리 가져와서 합계 계산
            for meal_time in ["아침", "점심", "저녁"]:
                meal_calories = db_instance.get_daily_calories(selected_date)
                meal_calories_value = 0  # 변수 초기화
                if meal_calories is not None and meal_calories[meal_time] is not None:
                    meal_calories_value = meal_calories[meal_time]
                daily_calories_text += f"{meal_time}: {meal_calories_value} kcal\n"
                total_calories += meal_calories_value  # 아침, 점심, 저녁 칼로리 누적
                        
            # total_calories가 None 또는 유효한 숫자(float)인지 확인하여 목표 달성율 계산
            if total_calories is not None and isinstance(total_calories, (float, int)):
                goal_rate = (total_calories / goal_calories) * 100
            else:
                print("칼로리 합계가 유효하지 않습니다.")
                return

            # 계산된 목표 달성율을 출력하거나 사용할 수 있도록 저장
            goal_rate_txt = f"{goal_rate:.2f} %"
            print(f"{selected_date}: {goal_rate_txt}%")
            self.goal_rate.setText(goal_rate_txt)
            
            combined_text = f"{selected_date}\n"
            self.select_date.setText(f"{selected_date}\n")
            self.daily_calories.setText(daily_calories_text)  # 레이블에 문자열 설정

        except Exception as e:
            print("목표 달성율을 계산하는 동안 오류 발생:", e)



        
        
    def delete_images(self):
        try:
            conn = db_instance.get_connection()
            cursor = conn.cursor()
            date = self.calendarWidget.selectedDate().toPyDate()

            # 아침, 점심, 저녁 이미지 모두 삭제
            for meal_type in ["아침", "점심", "저녁"]:
                db_instance.delete_meal_images(date, meal_type)

            messageBox = QMessageBox()
            messageBox.setText(f"Images deleted for {date}")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()

            # 이미지 목록을 갱신하여 이미지 삭제 후 화면을 업데이트합니다.
            self.update_screen()

        except Exception as e:
            print(f"Database error: {e}")

    
    def show_image_uploader(self):
        # 이미지 업로더를 보여줍니다.
        self.image_upload.show()
    
    def display_meal_image(self, selected_date, meal_type, image_label):
        try:
            # 해당 식사 시간대 이미지 가져오기
            image_path = db_instance.get_meal_image(selected_date, meal_type)

            if image_path:
                pixmap = QPixmap(image_path)
                image_label.setPixmap(pixmap)
                image_label.setScaledContents(True)
                image_label.setAlignment(Qt.AlignCenter)
            else:
                print(f"No {meal_type} img")

        except Exception as e:
            print(f"Error displaying {meal_type} image: {e}")

        
# 테스트용
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarWindow()
    window.show()
    sys.exit(app.exec())