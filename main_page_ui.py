# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 411, 581))
        self.label.setStyleSheet("background-color: rgb(239, 236, 232);\n"
"border-image: url(:/images/main.jpg);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 371, 541))
        self.label_2.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255,0), stop:1 rgba(255, 255, 255, 150));\n"
"border-radius:15px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.profile_image_2 = QtWidgets.QLabel(Form)
        self.profile_image_2.setGeometry(QtCore.QRect(170, 30, 131, 111))
        self.profile_image_2.setStyleSheet("border-radius: 30%;\n"
"background-color: rgba(195, 195, 195, 255);")
        self.profile_image_2.setText("")
        self.profile_image_2.setObjectName("profile_image_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 150, 351, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setStyleSheet("color: rgb(105, 118, 132);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(7, 7, 7, 7)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.calenderButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calenderButton.sizePolicy().hasHeightForWidth())
        self.calenderButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.calenderButton.setFont(font)
        self.calenderButton.setStyleSheet("QPushButton#calenderButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 200));\n"
"    color: rgba(105, 118, 132, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#calenderButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 226));\n"
"    color: rgba(131, 96, 53, 255); /* 호버 상태일 때의 글꼴 색상 변경 */\n"
"}\n"
"QPushButton#calenderButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.calenderButton.setObjectName("calenderButton")
        self.gridLayout.addWidget(self.calenderButton, 1, 1, 1, 1)
        self.goalEditButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goalEditButton.sizePolicy().hasHeightForWidth())
        self.goalEditButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.goalEditButton.setFont(font)
        self.goalEditButton.setStyleSheet("QPushButton#goalEditButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 100));\n"
"    color: rgba(105, 118, 132, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#goalEditButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 226));\n"
"    color: rgba(131, 96, 53, 255); /* 호버 상태일 때의 글꼴 색상 변경 */\n"
"}\n"
"QPushButton#goalEditButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.goalEditButton.setObjectName("goalEditButton")
        self.gridLayout.addWidget(self.goalEditButton, 0, 1, 1, 1)
        self.profileEditButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileEditButton.sizePolicy().hasHeightForWidth())
        self.profileEditButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.profileEditButton.setFont(font)
        self.profileEditButton.setStyleSheet("QPushButton#profileEditButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 200), stop: 1 rgba(255, 255, 255, 100));\n"
"    color: rgba(105, 118, 132, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#profileEditButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 226));\n"
"    color: rgba(131, 96, 53, 255); /* 호버 상태일 때의 글꼴 색상 변경 */\n"
"}\n"
"QPushButton#profileEditButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.profileEditButton.setObjectName("profileEditButton")
        self.gridLayout.addWidget(self.profileEditButton, 0, 0, 1, 1)
        self.uploadfoodButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadfoodButton.sizePolicy().hasHeightForWidth())
        self.uploadfoodButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.uploadfoodButton.setFont(font)
        self.uploadfoodButton.setStyleSheet("QPushButton#uploadfoodButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 200));\n"
"    color: rgba(105, 118, 132, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#uploadfoodButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 226));\n"
"    color: rgba(131, 96, 53, 255); /* 호버 상태일 때의 글꼴 색상 변경 */\n"
"}\n"
"QPushButton#uploadfoodButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.uploadfoodButton.setObjectName("uploadfoodButton")
        self.gridLayout.addWidget(self.uploadfoodButton, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.goal_content = QtWidgets.QLabel(Form)
        self.goal_content.setGeometry(QtCore.QRect(60, 350, 349, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goal_content.sizePolicy().hasHeightForWidth())
        self.goal_content.setSizePolicy(sizePolicy)
        self.goal_content.setStyleSheet("border-radius: 30%; /* 반지름을 크기의 50%로 설정하여 동그란 형태를 만듭니다. */\n"
"background-color: rgba(195, 195, 195, 70);")
        self.goal_content.setText("")
        self.goal_content.setObjectName("goal_content")
        self.goal = QtWidgets.QLabel(Form)
        self.goal.setGeometry(QtCore.QRect(150, 350, 162, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goal.sizePolicy().hasHeightForWidth())
        self.goal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.goal.setFont(font)
        self.goal.setStyleSheet("color: rgb(105, 118, 132);")
        self.goal.setAlignment(QtCore.Qt.AlignCenter)
        self.goal.setObjectName("goal")
        self.profile_image = QtWidgets.QLabel(Form)
        self.profile_image.setGeometry(QtCore.QRect(180, 30, 111, 111))
        self.profile_image.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.profile_image.setText("")
        self.profile_image.setObjectName("profile_image")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 380, 171, 46))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드OTF ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(105, 118, 132);")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.current_goal = QtWidgets.QLabel(Form)
        self.current_goal.setGeometry(QtCore.QRect(290, 500, 101, 46))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_goal.sizePolicy().hasHeightForWidth())
        self.current_goal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드OTF ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.current_goal.setFont(font)
        self.current_goal.setStyleSheet("border-radius: 30%;\n"
"color: rgb(105, 118, 132);\n"
"")
        self.current_goal.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.current_goal.setObjectName("current_goal")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name.setText(_translate("Form", "NAME"))
        self.calenderButton.setText(_translate("Form", "Calender View"))
        self.goalEditButton.setText(_translate("Form", "Goal edit"))
        self.profileEditButton.setText(_translate("Form", "Profile image edit"))
        self.uploadfoodButton.setText(_translate("Form", "Upload Food"))
        self.goal.setText(_translate("Form", "Goal"))
        self.label_3.setText(_translate("Form", "현재 목표는 "))
        self.current_goal.setText(_translate("Form", "9999"))
import res_rc
