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
    
    def save_image_data(self,user_id, image_name, image_path, meal_time, selected_date, calorie):
        try:
            cursor = self.conn.cursor()

            # 이미지 데이터 삽입 쿼리
            insert_query = """
            INSERT INTO images (user_id, image_name, image_path, meal_time, date, calories)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query, (user_id, image_name, image_path, meal_time, selected_date, calorie))
            self.conn.commit()

            print("이미지 데이터가 성공적으로 저장되었습니다.")
        except sqlite3.Error as e:
            print("이미지 데이터 저장 중 오류 발생:", str(e))

db_instance = DatabaseUtils()
