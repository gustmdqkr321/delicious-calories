11/3

myspl로 데이터베이스 연동해서 회원가입 시스템 구축이 목표

- login.ui와 createacc.ui 디자인까지 완성
  - 연동해보려 했으나 단순 loadui할 경우 이미지 리소스 파일이 정상작동하지 않음
- ui를 py로 변환하고 이 때 생기는 login_ui.py의 Ui_Form클래스를 불러와 메인에서 실행하도록 수정
  - ex.py


## ETC

```
E:\git_E\delicious-calories>C:/Users/dkxl1/anaconda3/Scripts/activate

(base) E:\git_E\delicious-calories>conda activate base

콘다로 인터프리터 설정해서 가상환경
```

QCssParser::parseColorValue: Specified color without alpha value but alpha given: 'rgb 105, 118, 132, 150

- rgb, rgba 파라미터 개수 오류 수정


```
pyuic5 -x your_ui_file.ui -o output_py_file.py

pyrcc5 res.qrc -o res_rc.py
```

pyuic5 -x login.ui -o login_ui.py

pyuic5 -x  createacc.ui -o createacc_ui.py

pyuic5 -x splash_screen.ui -o splash_screen_ui.py

pyuic5 my_ui_file.ui -o my_ui_file.py

pyuic5 main_page.ui -o main_page_ui.py

pyside6-uic splash_screen.ui -o splash_screen_ui.py

---

- 로그인 화면 뜨고 가입 버튼 클릭시 가입화면 뜸. 가입화면이나 로그인화면에서 입력을 콘솔로 출력까지 완료

## MYSQL

[설치 및 세팅](https://blog.naver.com/PostView.nhn?blogId=saegot&logNo=222453762728)

[MySQL 설정](https://blog.naver.com/chogar/221925309816)

````
http://localhost/phpmyadmin
````

사이트 접속시 

```
Forbidden
You don't have permission to access this resource.

Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.2.4 Server at localhost Port 80
```

에러 발생

ㅠㅠ xampp 삭제하고 다시 phpmyadmin 추가해서 설치해보기

[참고](https://blog.containerize.com/ko/how-to-setup-xampp-and-phpmyadmin-as-localhost-on-windows/)

```
우리 앱은 사용자가 음식 사진을 찍으면 칼로리 정보를 신속하게 제공하고, 개인 건강을 
관리하기 위한 캘린더 형태의 건강을 케어 도우미입니다. 캘린더 기능을 통해 사용자가 
자신이 섭취한 음식 사진들을 한눈에 볼 수 있도록 하고 날짜별로 자세한 식사 정보를 
조회할 수 있습니다.
이  캘린더는  사용자가  기간별로  자신의  식단을  쉽게  추적하고,  영양소  정보  및  칼로리 
소비량도  조회할  수  있습니다.  곧  사용자는  자신의  식사  기록을  통해  어떤  음식을  얼마나 
섭취했는지  확인하고  건강한  목표를  달성하기  위한  진행  상황을  파악할  수  있습니다.  또한 
앱  사용자들이  더  건강하고  밸런스  잡힌  식단을  쉽게  구성하고  관리할  수  있을  것입니다.  즉 
사용자가  자신의  식사  기록을  추적하고  개인적인  목표를  설정하여  건강한  라이프스타일을 
달성할  수  있습니다.
```



회원가입 시스템 구현 > https://m.blog.naver.com/bgpoilkj/221073079209

phpmyadmin 사용자 계정 생성 > http://yoonbumtae.com/?p=3541



>  사용자 계정 생성 후 가입하기 누르면 질의보내서 데이터베이스 업데이트 되는 부분 확인
>
>  다음 목표 : 로그인 기능할 때 데이터베이스의 이메일, 비밀번호 확인 후 정상 로그인
>
>  ​			가입하기 누르고 정상적으로 가입되면 알려주는 기능 필요(콘솔로 충분?)
>
>  ​		가입할 때도 이미 있는 이메일일 경우 거부하기

아 이메일 말고 아이디로 다 바꿔야 할듯,,이메일,,귀찮고 기니까,,

phpMyAdmin Auto_Increment 사용 > https://serpiko.tistory.com/559



## 11/4

현재까지 상황 및 목표

- 데베 생성 후 mysql 연결, 가입 가능 / 로그인,가입 ui 완

todo

- 로그인 가입 정상작동 - 현재는 다 가입되고 DB 올라감, 핸들링 추가하기
- 승꺼랑 합치기 - 완
- 레포 정리 - 완

승현

- 메인화면이랑 이미지 업로드, 프로필 수정 가져오기 - 완
  - UI 만들기
- 로그인 회원가입 핸들링 부분 합치기 - 완




## 11/5

todo

- 음식칼로리 이미지셋 > https://github.com/openfoodfacts
  - 간단한 카테고리의 음식만이라도 칼로리 인식 가능하게?
- 캘린더뷰 제작



fin

- 시작 화면 추가
- 메인UI 제작 및 연결



## 11/6

- mysql 건들다가 서버 터짐..ㅋㅋㅋ
- SQLite 쓰면 될듯, 업데이트 완



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
```

