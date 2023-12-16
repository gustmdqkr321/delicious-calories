# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_date.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 411, 581))
        self.label.setStyleSheet(u"background-color: rgb(239, 236, 232);\n"
"border-image: url(:/images/main.jpg);\n"
"border-radius:20px;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 40, 371, 541))
        self.label_2.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255,0), stop:1 rgba(255, 255, 255, 150));\n"
"border-radius:15px;")
        self.profile_image_2 = QLabel(Form)
        self.profile_image_2.setObjectName(u"profile_image_2")
        self.profile_image_2.setGeometry(QRect(170, 30, 131, 111))
        self.profile_image_2.setStyleSheet(u"border-radius: 30%;\n"
"background-color: rgba(195, 195, 195, 255);")
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 150, 351, 181))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.name = QLabel(self.verticalLayoutWidget)
        self.name.setObjectName(u"name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(20)
        font.setBold(True)
        self.name.setFont(font)
        self.name.setStyleSheet(u"color: rgb(105, 118, 132);")
        self.name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.name)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(7, 7, 7, 7)
        self.calenderButton = QPushButton(self.verticalLayoutWidget)
        self.calenderButton.setObjectName(u"calenderButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.calenderButton.sizePolicy().hasHeightForWidth())
        self.calenderButton.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Microsoft JhengHei UI"])
        font1.setPointSize(8)
        font1.setBold(True)
        self.calenderButton.setFont(font1)
        self.calenderButton.setStyleSheet(u"QPushButton#calenderButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 200));\n"
"    color: rgba(105, 118, 132, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#calenderButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 226));\n"
"    color: rgba(131, 96, 53, 255); /* \ud638\ubc84 \uc0c1\ud0dc\uc77c \ub54c\uc758 \uae00\uaf34 \uc0c9\uc0c1 \ubcc0\uacbd */\n"
"}\n"
"QPushButton#calenderButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.calenderButton, 1, 1, 1, 1)

        self.goalEditButton = QPushButton(self.verticalLayoutWidget)
        self.goalEditButton.setObjectName(u"goalEditButton")
        sizePolicy2.setHeightForWidth(self.goalEditButton.sizePolicy().hasHeightForWidth())
        self.goalEditButton.setSizePolicy(sizePolicy2)
        self.goalEditButton.setFont(font1)
        self.goalEditButton.setStyleSheet(u"QPushButton#goalEditButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 100));\n"
"    color: rgba(105, 118, 132, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#goalEditButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 226));\n"
"    color: rgba(131, 96, 53, 255); /* \ud638\ubc84 \uc0c1\ud0dc\uc77c \ub54c\uc758 \uae00\uaf34 \uc0c9\uc0c1 \ubcc0\uacbd */\n"
"}\n"
"QPushButton#goalEditButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.goalEditButton, 0, 1, 1, 1)

        self.profileEditButton = QPushButton(self.verticalLayoutWidget)
        self.profileEditButton.setObjectName(u"profileEditButton")
        sizePolicy2.setHeightForWidth(self.profileEditButton.sizePolicy().hasHeightForWidth())
        self.profileEditButton.setSizePolicy(sizePolicy2)
        self.profileEditButton.setFont(font1)
        self.profileEditButton.setStyleSheet(u"QPushButton#profileEditButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 200), stop: 1 rgba(255, 255, 255, 100));\n"
"    color: rgba(105, 118, 132, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#profileEditButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 226));\n"
"    color: rgba(131, 96, 53, 255); /* \ud638\ubc84 \uc0c1\ud0dc\uc77c \ub54c\uc758 \uae00\uaf34 \uc0c9\uc0c1 \ubcc0\uacbd */\n"
"}\n"
"QPushButton#profileEditButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.profileEditButton, 0, 0, 1, 1)

        self.uploadfoodButton = QPushButton(self.verticalLayoutWidget)
        self.uploadfoodButton.setObjectName(u"uploadfoodButton")
        sizePolicy2.setHeightForWidth(self.uploadfoodButton.sizePolicy().hasHeightForWidth())
        self.uploadfoodButton.setSizePolicy(sizePolicy2)
        self.uploadfoodButton.setFont(font1)
        self.uploadfoodButton.setStyleSheet(u"QPushButton#uploadfoodButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 200));\n"
"    color: rgba(105, 118, 132, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#uploadfoodButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(255, 255, 255, 100), stop: 1 rgba(255, 255, 255, 226));\n"
"    color: rgba(131, 96, 53, 255); /* \ud638\ubc84 \uc0c1\ud0dc\uc77c \ub54c\uc758 \uae00\uaf34 \uc0c9\uc0c1 \ubcc0\uacbd */\n"
"}\n"
"QPushButton#uploadfoodButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.uploadfoodButton, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.goal_content = QLabel(Form)
        self.goal_content.setObjectName(u"goal_content")
        self.goal_content.setGeometry(QRect(60, 350, 349, 211))
        sizePolicy2.setHeightForWidth(self.goal_content.sizePolicy().hasHeightForWidth())
        self.goal_content.setSizePolicy(sizePolicy2)
        self.goal_content.setStyleSheet(u"border-radius: 30%; /* \ubc18\uc9c0\ub984\uc744 \ud06c\uae30\uc758 50%\ub85c \uc124\uc815\ud558\uc5ec \ub3d9\uadf8\ub780 \ud615\ud0dc\ub97c \ub9cc\ub4ed\ub2c8\ub2e4. */\n"
"background-color: rgba(195, 195, 195, 70);")
        self.goal = QLabel(Form)
        self.goal.setObjectName(u"goal")
        self.goal.setGeometry(QRect(150, 350, 162, 24))
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.goal.sizePolicy().hasHeightForWidth())
        self.goal.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamilies([u"Corbel"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.goal.setFont(font2)
        self.goal.setStyleSheet(u"color: rgb(105, 118, 132);")
        self.goal.setAlignment(Qt.AlignCenter)
        self.profile_image = QLabel(Form)
        self.profile_image.setObjectName(u"profile_image")
        self.profile_image.setGeometry(QRect(180, 30, 111, 111))
        self.profile_image.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.profile_image_2.setText("")
        self.name.setText(QCoreApplication.translate("Form", u"NAME", None))
        self.calenderButton.setText(QCoreApplication.translate("Form", u"Calender View", None))
        self.goalEditButton.setText(QCoreApplication.translate("Form", u"Goal edit", None))
        self.profileEditButton.setText(QCoreApplication.translate("Form", u"Profile image edit", None))
        self.uploadfoodButton.setText(QCoreApplication.translate("Form", u"Upload Food", None))
        self.goal_content.setText("")
        self.goal.setText(QCoreApplication.translate("Form", u"Goal", None))
        self.profile_image.setText("")
    # retranslateUi

