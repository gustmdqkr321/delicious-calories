# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calendarView.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 700)
        self.calendarWidget = QCalendarWidget(Form)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(20, 120, 531, 481))
        self.calendarWidget.setStyleSheet(u"font:10pt;")
        self.imageListWidget = QListWidget(Form)
        self.imageListWidget.setObjectName(u"imageListWidget")
        self.imageListWidget.setGeometry(QRect(570, 160, 411, 401))
        self.imageListWidget.setStyleSheet(u"font:12pt;")
        self.deleteButton = QPushButton(Form)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(570, 570, 411, 28))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet(u"border-radius:10px;\n"
"background : #0076d2;\n"
"color:white;\n"
"font:11pt;")
        self.uploadButton = QPushButton(Form)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.setGeometry(QRect(810, 120, 171, 28))
        self.uploadButton.setStyleSheet(u"border-radius:10px;\n"
"background : #0076d2;\n"
"color:white;\n"
"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1001, 101))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(24)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font-size : 24pt;\n"
"background : #0076d2;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.background = QLabel(Form)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(-10, 0, 1011, 701))
        self.background.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.breakfast = QLabel(Form)
        self.breakfast.setObjectName(u"breakfast")
        self.breakfast.setGeometry(QRect(580, 180, 181, 111))
        font2 = QFont()
        font2.setFamilies([u"\ub098\ub214\uc2a4\ud018\uc5b4OTF ExtraBold"])
        font2.setPointSize(17)
        self.breakfast.setFont(font2)
        self.breakfast.setStyleSheet(u"background-color: rgb(0, 118, 210);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.breakfast.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.breakfast_img = QLabel(Form)
        self.breakfast_img.setObjectName(u"breakfast_img")
        self.breakfast_img.setGeometry(QRect(590, 210, 161, 71))
        self.breakfast_img.setFont(font2)
        self.breakfast_img.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20%;\n"
"")
        self.breakfast_img.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.breakfast_3 = QLabel(Form)
        self.breakfast_3.setObjectName(u"breakfast_3")
        self.breakfast_3.setGeometry(QRect(690, 350, 161, 71))
        self.breakfast_3.setFont(font2)
        self.breakfast_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20%;\n"
"")
        self.breakfast_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lunch = QLabel(Form)
        self.lunch.setObjectName(u"lunch")
        self.lunch.setGeometry(QRect(580, 310, 181, 111))
        self.lunch.setFont(font2)
        self.lunch.setStyleSheet(u"background-color: rgb(0, 118, 210);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.lunch.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.lunch_img = QLabel(Form)
        self.lunch_img.setObjectName(u"lunch_img")
        self.lunch_img.setGeometry(QRect(590, 340, 161, 71))
        self.lunch_img.setFont(font2)
        self.lunch_img.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20%;\n"
"")
        self.lunch_img.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lunch_2 = QLabel(Form)
        self.lunch_2.setObjectName(u"lunch_2")
        self.lunch_2.setGeometry(QRect(580, 440, 181, 111))
        self.lunch_2.setFont(font2)
        self.lunch_2.setStyleSheet(u"background-color: rgb(0, 118, 210);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.lunch_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.dinner_img = QLabel(Form)
        self.dinner_img.setObjectName(u"dinner_img")
        self.dinner_img.setGeometry(QRect(590, 470, 161, 71))
        self.dinner_img.setFont(font2)
        self.dinner_img.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20%;\n"
"")
        self.dinner_img.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label2 = QLabel(Form)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(770, 180, 191, 371))
        self.label2.setFont(font2)
        self.label2.setStyleSheet(u"background-color: rgb(0, 118, 210);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.goal_rate = QLabel(Form)
        self.goal_rate.setObjectName(u"goal_rate")
        self.goal_rate.setGeometry(QRect(790, 320, 101, 81))
        font3 = QFont()
        font3.setFamilies([u"Arial Black"])
        font3.setPointSize(21)
        self.goal_rate.setFont(font3)
        self.goal_rate.setStyleSheet(u"color: rgb(255, 255, 127);")
        self.updateButton = QPushButton(Form)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setGeometry(QRect(570, 120, 231, 28))
        font4 = QFont()
        font4.setFamilies([u"Consolas"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.updateButton.setFont(font4)
        self.updateButton.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 118, 210);\n"
"")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(810, 240, 111, 41))
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift"])
        font5.setPointSize(16)
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.select_date = QLabel(Form)
        self.select_date.setObjectName(u"select_date")
        self.select_date.setGeometry(QRect(790, 390, 131, 41))
        font6 = QFont()
        font6.setFamilies([u"Bahnschrift"])
        font6.setPointSize(11)
        self.select_date.setFont(font6)
        self.select_date.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tmp = QLabel(Form)
        self.tmp.setObjectName(u"tmp")
        self.tmp.setGeometry(QRect(780, 220, 171, 71))
        font7 = QFont()
        font7.setFamilies([u"\ub098\ub214\ubc14\ub978\ud39cOTF"])
        font7.setPointSize(9)
        font7.setBold(True)
        font7.setUnderline(False)
        self.tmp.setFont(font7)
        self.tmp.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"border-radius: 20%;\n"
"")
        self.tmp.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(890, 280, 161, 171))
        font8 = QFont()
        font8.setFamilies([u"Arial Black"])
        font8.setPointSize(28)
        self.label_2.setFont(font8)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 127);")
        self.daily_calories = QLabel(Form)
        self.daily_calories.setObjectName(u"daily_calories")
        self.daily_calories.setGeometry(QRect(790, 420, 131, 121))
        self.daily_calories.setFont(font6)
        self.daily_calories.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.background.raise_()
        self.calendarWidget.raise_()
        self.imageListWidget.raise_()
        self.deleteButton.raise_()
        self.uploadButton.raise_()
        self.label.raise_()
        self.breakfast.raise_()
        self.breakfast_img.raise_()
        self.breakfast_3.raise_()
        self.lunch.raise_()
        self.lunch_img.raise_()
        self.lunch_2.raise_()
        self.dinner_img.raise_()
        self.label2.raise_()
        self.goal_rate.raise_()
        self.updateButton.raise_()
        self.select_date.raise_()
        self.tmp.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.daily_calories.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.deleteButton.setText(QCoreApplication.translate("Form", u"Data deleted : \"date\" images deleted", None))
        self.uploadButton.setText(QCoreApplication.translate("Form", u"upload image", None))
        self.label.setText(QCoreApplication.translate("Form", u"Calendar View", None))
        self.background.setText("")
        self.breakfast.setText(QCoreApplication.translate("Form", u"\uc544\uce68", None))
        self.breakfast_img.setText("")
        self.breakfast_3.setText("")
        self.lunch.setText(QCoreApplication.translate("Form", u"\uc810\uc2ec", None))
        self.lunch_img.setText("")
        self.lunch_2.setText(QCoreApplication.translate("Form", u"\uc800\ub141", None))
        self.dinner_img.setText("")
        self.label2.setText(QCoreApplication.translate("Form", u"\ubaa9\ud45c\ub2ec\uc131\ub960", None))
        self.goal_rate.setText(QCoreApplication.translate("Form", u"100", None))
        self.updateButton.setText(QCoreApplication.translate("Form", u"CHANGE UPDATE", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"2000-2500", None))
        self.select_date.setText(QCoreApplication.translate("Form", u"cal calories", None))
        self.tmp.setText(QCoreApplication.translate("Form", u"\ud558\ub8e8 \uad8c\uc7a5 \uce7c\ub85c\ub9ac", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"%", None))
        self.daily_calories.setText(QCoreApplication.translate("Form", u"cal calories", None))
    # retranslateUi

