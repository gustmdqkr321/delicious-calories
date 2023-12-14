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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 700)
        self.calendarWidget = QCalendarWidget(Form)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(20, 120, 531, 481))
        self.calendarWidget.setStyleSheet(u"font:10pt;")
        self.tasksListWidget = QListWidget(Form)
        self.tasksListWidget.setObjectName(u"tasksListWidget")
        self.tasksListWidget.setGeometry(QRect(570, 160, 411, 401))
        self.tasksListWidget.setStyleSheet(u"font:12pt;")
        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(570, 570, 411, 28))
        self.saveButton.setStyleSheet(u"border-radius:10px;\n"
"background : #0076d2;\n"
"color:white;\n"
"font:11pt;")
        self.addButton = QPushButton(Form)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(880, 120, 101, 28))
        self.addButton.setStyleSheet(u"border-radius:10px;\n"
"background : #0076d2;\n"
"color:white;\n"
"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1001, 101))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(24)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size : 24pt;\n"
"background : #0076d2;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.taskLineEdit = QLineEdit(Form)
        self.taskLineEdit.setObjectName(u"taskLineEdit")
        self.taskLineEdit.setGeometry(QRect(570, 120, 291, 31))
        self.taskLineEdit.setStyleSheet(u"font:12pt;")
        self.background = QLabel(Form)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(-10, 0, 1011, 701))
        self.background.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.background.raise_()
        self.calendarWidget.raise_()
        self.tasksListWidget.raise_()
        self.saveButton.raise_()
        self.addButton.raise_()
        self.label.raise_()
        self.taskLineEdit.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save Changes", None))
        self.addButton.setText(QCoreApplication.translate("Form", u"Add new", None))
        self.label.setText(QCoreApplication.translate("Form", u"Calendar View", None))
        self.background.setText("")
    # retranslateUi

