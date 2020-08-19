# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import app.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(200, 280)
        MainWindow.setMinimumSize(QSize(200, 280))
        MainWindow.setMaximumSize(QSize(200, 280))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/image/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(200, 280))
        self.centralwidget.setMaximumSize(QSize(200, 280))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 201, 291))
        self.frame.setMinimumSize(QSize(201, 291))
        self.frame.setMaximumSize(QSize(201, 291))
        self.frame.setStyleSheet(u"/*background-color: #E6E6FA;*/\n"
"background-color: #836FFF;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 322, 291))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.gridLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(320, 289))
        self.frame_2.setMaximumSize(QSize(320, 289))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.frame_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 120, 181, 151))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn1 = QPushButton(self.gridLayoutWidget_2)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btn1, 5, 0, 1, 1)

        self.btnParent1 = QPushButton(self.gridLayoutWidget_2)
        self.btnParent1.setObjectName(u"btnParent1")
        self.btnParent1.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btnParent1, 0, 1, 1, 1)

        self.btn7 = QPushButton(self.gridLayoutWidget_2)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btn7, 1, 0, 1, 1)

        self.btnVirg = QPushButton(self.gridLayoutWidget_2)
        self.btnVirg.setObjectName(u"btnVirg")
        self.btnVirg.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btnVirg, 6, 2, 1, 1)

        self.btn3 = QPushButton(self.gridLayoutWidget_2)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btn3, 5, 2, 1, 1)

        self.btnClear = QPushButton(self.gridLayoutWidget_2)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #FF0000;\n"
"background-color: #7A67EE;\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.btnClear, 0, 0, 1, 1)

        self.btn4 = QPushButton(self.gridLayoutWidget_2)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btn4, 4, 0, 1, 1)

        self.btnMult = QPushButton(self.gridLayoutWidget_2)
        self.btnMult.setObjectName(u"btnMult")
        self.btnMult.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btnMult, 1, 3, 1, 1)

        self.btnResult = QPushButton(self.gridLayoutWidget_2)
        self.btnResult.setObjectName(u"btnResult")
        self.btnResult.setBaseSize(QSize(0, 200))
        self.btnResult.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btnResult, 6, 3, 1, 1)

        self.btn9 = QPushButton(self.gridLayoutWidget_2)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btn9, 1, 2, 1, 1)

        self.btn5 = QPushButton(self.gridLayoutWidget_2)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btn5, 4, 1, 1, 1)

        self.btnAdic = QPushButton(self.gridLayoutWidget_2)
        self.btnAdic.setObjectName(u"btnAdic")
        self.btnAdic.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btnAdic, 5, 3, 1, 1)

        self.btn2 = QPushButton(self.gridLayoutWidget_2)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btn2, 5, 1, 1, 1)

        self.btn8 = QPushButton(self.gridLayoutWidget_2)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btn8, 1, 1, 1, 1)

        self.btnDiv = QPushButton(self.gridLayoutWidget_2)
        self.btnDiv.setObjectName(u"btnDiv")
        self.btnDiv.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btnDiv, 0, 3, 1, 1)

        self.btnSub = QPushButton(self.gridLayoutWidget_2)
        self.btnSub.setObjectName(u"btnSub")
        self.btnSub.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btnSub, 4, 3, 1, 1)

        self.btn0 = QPushButton(self.gridLayoutWidget_2)
        self.btn0.setObjectName(u"btn0")
        self.btn0.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btn0, 6, 0, 1, 2)

        self.btnParent2 = QPushButton(self.gridLayoutWidget_2)
        self.btnParent2.setObjectName(u"btnParent2")
        self.btnParent2.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btnParent2, 0, 2, 1, 1)

        self.btn6 = QPushButton(self.gridLayoutWidget_2)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #ffffff;\n"
"background-color: #7A67EE;")

        self.gridLayout_2.addWidget(self.btn6, 4, 2, 1, 1)

        self.display = QLCDNumber(self.frame_2)
        self.display.setObjectName(u"display")
        self.display.setGeometry(QRect(10, 10, 181, 101))
        self.display.setMinimumSize(QSize(181, 101))
        self.display.setMaximumSize(QSize(181, 101))
        self.display.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #6959CD;\n"
"")

        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btnParent1.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.btn7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btnVirg.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btnMult.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btnResult.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btnAdic.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btnDiv.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btnSub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnParent2.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.btn6.setText(QCoreApplication.translate("MainWindow", u"6", None))
    # retranslateUi

