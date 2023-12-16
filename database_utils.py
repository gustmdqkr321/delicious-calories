# database_utils.py

import sqlite3

class DatabaseUtils:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseUtils, cls).__new__(cls)
            cls._instance.conn = None
            cls._instance.user_id = None  # 사용자 아이디를 저장할 변수
        return cls._instance

    def create_connection(self):
        if self.conn is None:  # 이미 연결이 설정되어 있으면 다시 설정하지 않음
            db_file = "userdata.db"
            self.conn = sqlite3.connect(db_file)
            self.conn.row_factory = sqlite3.Row  # 결과를 딕셔너리로 가져오도록 설정

    def get_connection(self):
        self.create_connection()  # sqlite_connection 메서드를 호출하여 연결을 설정
        return self.conn
    
    def check_login(self, user_id, password):
        try:
            cursor = self.conn.cursor()

            # 로그인 정보 확인 쿼리
            query = "SELECT * FROM users WHERE ID = ? AND password = ?"
            data = (user_id, password)
            cursor.execute(query, data)
            result = cursor.fetchone()
            
            if result:
                print(f"Successfully logged in with ID: {user_id} and password: {password}")
                return True
            else:
                print("Login failed. Invalid credentials.")
                return False
        except sqlite3.Error as e:
            print("Failed to connect to SQLite database:", str(e))
            return False
    
    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def get_user_name(self):
        if self.user_id is not None:
            cursor = self.conn.cursor()
            cursor.execute("SELECT username FROM users WHERE id = ?", (self.user_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
        return None

    def save_user_profile_image_path(self, image_path):
        cursor = self.conn.cursor()
        try:
            cursor.execute("UPDATE users SET profile_image_path = ? WHERE id = ?", (image_path, self.user_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error updating user profile image path:", str(e))
    
    def save_image_data(self, user_id, image_name, image_path, meal_time, selected_date, calorie):
        try:
            cursor = self.conn.cursor()

            # 이미지 데이터 삽입 쿼리
            insert_query = """
            INSERT INTO images (user_id, image_name, image_path, meal_time, date, calories)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query, (user_id, image_name, image_path, meal_time, selected_date, calorie))
            self.conn.commit()

            print(f"이미지 데이터가 성공적으로 저장되었습니다. (사용자 ID: {user_id}, 이미지 이름: {image_name}, 이미지 경로: {image_path}, 식사 시간대: {meal_time}, 날짜: {selected_date}, 칼로리: {calorie})")
        except sqlite3.Error as e:
            print("이미지 데이터 저장 중 오류 발생:", str(e))
    
    def set_goal(self, goal):
        cursor = self.conn.cursor()
        try:
            cursor.execute("UPDATE users SET goal = ? WHERE id = ?", (goal, self.user_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error updating user goal:", str(e))
            
    def get_goal(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT goal FROM users WHERE id = ?", (self.user_id,))
        result = cursor.fetchone()
        
        if result is not None and result[0] is not None:
            return result[0]
        else:
            print("목표 칼로리가 None입니다. 기본값 1500을 반환합니다.")
            return 1500
    
    def get_user_profile_image_path(self):
        try:
            cursor = self.conn.cursor()

            # 사용자 ID에 해당하는 프로필 이미지 경로 가져오기
            query = "SELECT profile_image_path FROM users WHERE id = ?"
            data = (self.user_id,)
            cursor.execute(query, data)
            result = cursor.fetchone()

            if result:
                return result[0]  # 프로필 이미지 경로 반환
            else:
                return None  # 이미지가 없으면 None 반환

        except sqlite3.Error as e:
            print("Error fetching profile image path:", str(e))
            return None
    
    def get_meal_image(self, selected_date, meal_time):
        try:
            cursor = self.conn.cursor()

            # 사용자 ID, 선택한 날짜, 및 식사 시간대에 해당하는 이미지 가져오기
            query = "SELECT image_path FROM images WHERE user_id = ? AND date = ? AND meal_time = ?"
            data = (self.user_id, selected_date, meal_time)
            cursor.execute(query, data)
            result = cursor.fetchone()

            if result:
                return result[0]  # 이미지 경로 반환
            else:
                return None  # 이미지가 없으면 None 반환

        except sqlite3.Error as e:
            print(f"Error fetching {meal_time} image:", str(e))
            return None
        
    def delete_meal_images(self, date, meal_type):
        try:
            cursor = self.conn.cursor()

            # 사용자 ID와 선택한 날짜, 식사 시간대에 해당하는 이미지 삭제
            query = "DELETE FROM images WHERE user_id = ? AND date = ? AND meal_time = ?"
            data = (self.user_id, date, meal_type)
            cursor.execute(query, data)
            self.conn.commit()

        except sqlite3.Error as e:
            print(f"Error deleting {meal_type} images:", str(e))
    
    def get_daily_calories(self, selected_date):
        try:
            cursor = self.conn.cursor()
            daily_calories = {
                '아침': 0,
                '점심': 0,
                '저녁': 0
            }

            for meal_time in daily_calories.keys():
                # 사용자 ID, 선택한 날짜, 및 식사 시간대에 해당하는 칼로리 합계 가져오기
                query = "SELECT SUM(CAST(calories AS FLOAT)) FROM images WHERE user_id = ? AND date = ? AND meal_time = ?"
                data = (self.user_id, selected_date, meal_time)
                cursor.execute(query, data)
                result = cursor.fetchone()

                if result and result[0] is not None:
                    daily_calories[meal_time] = float(result[0])

            return daily_calories

        except sqlite3.Error as e:
            print("Error calculating total calories by meal:", str(e))
            return None


            
    
db_instance = DatabaseUtils()
