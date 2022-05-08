# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(440, 330)
        MainWindow.setMinimumSize(QSize(440, 330))
        MainWindow.setMaximumSize(QSize(440, 340))
        MainWindow.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 441, 381))
        self.frame.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-radius:25px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_btns = QFrame(self.frame)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setGeometry(QRect(360, 0, 81, 31))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_btns)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_max = QPushButton(self.frame_btns)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setMinimumSize(QSize(16, 16))
        self.btn_max.setMaximumSize(QSize(17, 17))
        self.btn_max.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color:rgb(85,255,127);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(85,255,127,150);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_max)

        self.btn_min = QPushButton(self.frame_btns)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setMinimumSize(QSize(16, 16))
        self.btn_min.setMaximumSize(QSize(17, 17))
        self.btn_min.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color:rgb(255,170,0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(255,170,0,150);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_min)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color:rgb(255,0,0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(255,0,0,150);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_close)

        self.caminho = QLineEdit(self.frame)
        self.caminho.setObjectName(u"caminho")
        self.caminho.setGeometry(QRect(40, 170, 251, 31))
        self.caminho.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border:none;\n"
"border-radius:15px;")
        self.caminho.setFrame(True)
        self.btn_organizar = QPushButton(self.frame)
        self.btn_organizar.setObjectName(u"btn_organizar")
        self.btn_organizar.setGeometry(QRect(130, 250, 181, 31))
        self.btn_organizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_organizar.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:15px;\n"
"	background-color: rgb(245, 234, 114);\n"
"	color:black;	\n"
"	\n"
"	font: 57 10pt \"JetBrainsMono Nerd Font Mono\";\n"
"}")
        self.btn_abrir = QPushButton(self.frame)
        self.btn_abrir.setObjectName(u"btn_abrir")
        self.btn_abrir.setGeometry(QRect(300, 170, 111, 31))
        self.btn_abrir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_abrir.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:15px;\n"
"	background-color: rgb(245, 234, 114);\n"
"	color:black;	\n"
"	\n"
"	font: 57 10pt \"JetBrainsMono Nerd Font Mono\";\n"
"}")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 40, 141, 101))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_max.setText("")
#if QT_CONFIG(tooltip)
        self.btn_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_min.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.caminho.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta", None))
        self.btn_organizar.setText(QCoreApplication.translate("MainWindow", u"Organizar", None))
        self.btn_abrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"img\logo.png\" /></p></body></html>", None))
    # retranslateUi

