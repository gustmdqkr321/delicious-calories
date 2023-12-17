# delicious-calories

> KMU Software Architecture course proj

Delicious-Calories is a health management application that allows users to quickly retrieve calorie information of food by taking a picture. The app provides a calendar feature for users to manage their health.

## Features

- **Calorie Information**: Snap a picture of your meal, and the app will provide you with calorie information for each food item.
- **Calendar View**: Keep track of your daily health activities and meals using the built-in calendar.
- **Profile Management**: Edit your profile picture and set your health goals.
- **User Authentication**: Create an account and log in to access personalized features.

## Installation and Usage

1. Clone the repository to your local machine.

2. Install the required dependencies.

3. Run the application.

   ```
   python main.py
   ```

## Dependencies

```
Qt version: 5.15.2
PySide version: 6.6.0
Python version: 3.11.5 | packaged by Anaconda
MySQL version: 8.2.0
tensorflow 2.15.0
googletrans 4.0.0-rc.1
```

## Database Setup

Before running the application, make sure to configure the database settings in `database_utils.py`.

## Test Account

```
ID : 123
이름 : admin
비번 : 123
```

## Directory Structure

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



# Demo
![SA](https://github.com/hhzzzk/delicious-calories/assets/67236054/210c96c7-36eb-481c-b15f-51b3791f74ec)
![SA (1)](https://github.com/hhzzzk/delicious-calories/assets/67236054/e4f50430-f0c9-4c53-9932-bc293b18ad43)
![SA (2)](https://github.com/hhzzzk/delicious-calories/assets/67236054/b45e152c-a91d-4695-a5d9-a0dba13a1e58)
![SA (3)](https://github.com/hhzzzk/delicious-calories/assets/67236054/0a74dc04-8176-44a7-ae6b-a4168725955f)
![SA (4)](https://github.com/hhzzzk/delicious-calories/assets/67236054/4dbae6d7-be96-4daf-a19c-ec5aa2ade329)


