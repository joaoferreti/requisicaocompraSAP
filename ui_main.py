# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'requisicao.ui'
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
        MainWindow.resize(671, 385)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 58, 86, 255), stop:1 rgba(0, 106, 155, 255));")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-radius: 10px; \n"
"	border: 1px solid white;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,157,235)\n"
"	\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px; \n"
"	border: 1px solid white;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_path = QLineEdit(self.frame_2)
        self.txt_path.setObjectName(u"txt_path")
        self.txt_path.setMinimumSize(QSize(0, 20))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.txt_path.setFont(font)
        self.txt_path.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_path)

        self.btn_abrir = QPushButton(self.frame_2)
        self.btn_abrir.setObjectName(u"btn_abrir")
        self.btn_abrir.setMinimumSize(QSize(60, 20))
        font1 = QFont()
        font1.setPointSize(10)
        self.btn_abrir.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btn_abrir)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(160, 20))
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-radius: 10px; \n"
"	border: 1px solid white;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,157,235)\n"
"	\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_gerar = QPushButton(self.frame_3)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setMinimumSize(QSize(120, 20))
        self.btn_gerar.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.btn_gerar, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Criar Requisi\u00e7\u00e3o de Compra</span></p></body></html>", None))
        self.txt_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a Planilha --->", None))
        self.btn_abrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar", None))
    # retranslateUi

