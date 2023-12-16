# delicious-calories

> KMU Software Architecture course proj

Delicious-Calories is a health management application that allows users to quickly retrieve calorie information of food by taking a picture. The app provides a calendar feature for users to manage their health.

- 이미지 추가
- 구조 추가
## 테스트 아이디 비번

```
ID : 123
이름 : admin
비번 : 123
```
## 실행

main.py 실행

## 구조

```
├── main.py
├── start_page.py
├── loginwindow.py
│   ├── create_account────success/fail
│   └── login─────────────success/fail
└── main_page.py
│   ├── profile image edit────
│   ├── goal edit─────────────
│   ├── Upload Food───────────image_upload.py
│   └── Calender View─────────
────────────────────────────────────
UI
────────────────────────────────────
splash_screen_ui.py
login_ui.py
createacc_ui.py
main_page_ui.py

res_rc.py
start_rc.py
────────────────────────────────────
DB
────────────────────────────────────
datebase_utils.py

```

## version

```
Qt version: 5.15.2
PySide version: 6.6.0
Python version: 3.11.5 | packaged by Anaconda
MySQL version: 8.2.0
tensorflow 2.15.0
googletrans 4.0.0-rc.1
```

