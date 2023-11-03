11/3

- myspl로 데이터베이스 연동해서 회원가입 시스템 구축이 목표
- login.ui와 createacc.ui 디자인까지 완성
  - 연동해보려 했으나 단순 loadui할 경우 이미지 리소스 파일이 정상작동하지 않음
- ui를 py로 변환하고 이 때 생기는 login_ui.py의 Ui_Form클래스를 불러와 메인에서 실행하도록 수정
  - ex.py



> 언제 연동해...버튼이름같은거 정리해야 할듯. 소셜로 로그인기능까지 가능할라나;;



## 실행

```
E:\git_E\delicious-calories>C:/Users/dkxl1/anaconda3/Scripts/activate

(base) E:\git_E\delicious-calories>conda activate base

콘다로 인터프리터 설정해서 가상환경
```

QCssParser::parseColorValue: Specified color without alpha value but alpha given: 'rgb 105, 118, 132, 150

- rgb, rgba 파라미터 개수 오류 수정


```
pyuic5 -x your_ui_file.ui -o output_py_file.py
```



## 굿

현재까지 현황

- 로그인 화면 뜨고 가입 버튼 클릭시 가입화면 뜸. 가입화면이나 로그인화면에서 입력을 콘솔로 출력까지 완료
- XAMPP를 이용해 MYSQL을 사용해보자

## MYSQL

[설치 및 세팅](https://blog.naver.com/PostView.nhn?blogId=saegot&logNo=222453762728)

[MySQL 설정](https://blog.naver.com/chogar/221925309816)

````
http://localhost/phpmyadmin
````

