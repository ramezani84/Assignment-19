# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 550)
        MainWindow.setStyleSheet(u"background-image: url(\"background.jpg\");")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(36)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_1, 0, 0, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_2, 0, 1, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_3, 0, 2, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_4, 0, 3, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_5, 1, 0, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_6, 1, 1, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_7, 1, 2, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_8, 1, 3, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_9, 2, 0, 1, 1)

        self.btn_10 = QPushButton(self.centralwidget)
        self.btn_10.setObjectName(u"btn_10")
        sizePolicy.setHeightForWidth(self.btn_10.sizePolicy().hasHeightForWidth())
        self.btn_10.setSizePolicy(sizePolicy)
        self.btn_10.setFont(font)
        self.btn_10.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_10, 2, 1, 1, 1)

        self.btn_11 = QPushButton(self.centralwidget)
        self.btn_11.setObjectName(u"btn_11")
        sizePolicy.setHeightForWidth(self.btn_11.sizePolicy().hasHeightForWidth())
        self.btn_11.setSizePolicy(sizePolicy)
        self.btn_11.setFont(font)
        self.btn_11.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_11, 2, 2, 1, 1)

        self.btn_12 = QPushButton(self.centralwidget)
        self.btn_12.setObjectName(u"btn_12")
        sizePolicy.setHeightForWidth(self.btn_12.sizePolicy().hasHeightForWidth())
        self.btn_12.setSizePolicy(sizePolicy)
        self.btn_12.setFont(font)
        self.btn_12.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_12, 2, 3, 1, 1)

        self.btn_13 = QPushButton(self.centralwidget)
        self.btn_13.setObjectName(u"btn_13")
        sizePolicy.setHeightForWidth(self.btn_13.sizePolicy().hasHeightForWidth())
        self.btn_13.setSizePolicy(sizePolicy)
        self.btn_13.setFont(font)
        self.btn_13.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_13, 3, 0, 1, 1)

        self.btn_14 = QPushButton(self.centralwidget)
        self.btn_14.setObjectName(u"btn_14")
        sizePolicy.setHeightForWidth(self.btn_14.sizePolicy().hasHeightForWidth())
        self.btn_14.setSizePolicy(sizePolicy)
        self.btn_14.setFont(font)
        self.btn_14.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_14, 3, 1, 1, 1)

        self.btn_15 = QPushButton(self.centralwidget)
        self.btn_15.setObjectName(u"btn_15")
        sizePolicy.setHeightForWidth(self.btn_15.sizePolicy().hasHeightForWidth())
        self.btn_15.setSizePolicy(sizePolicy)
        self.btn_15.setFont(font)
        self.btn_15.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_15, 3, 2, 1, 1)

        self.btn_16 = QPushButton(self.centralwidget)
        self.btn_16.setObjectName(u"btn_16")
        sizePolicy.setHeightForWidth(self.btn_16.sizePolicy().hasHeightForWidth())
        self.btn_16.setSizePolicy(sizePolicy)
        self.btn_16.setFont(font)
        self.btn_16.setStyleSheet(u"/* From https://css.glass */\n"
"color: rgb(234, 234, 69);\n"
"background: rgba(172, 172, 172, 0.41);\n"
"border-radius: 10px;\n"
"box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n"
"backdrop-filter: blur(5px);\n"
"-webkit-backdrop-filter: blur(5px);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 5, 9);")

        self.gridLayout.addWidget(self.btn_16, 3, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 540, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"puzzle15", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.btn_11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.btn_12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.btn_13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.btn_14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.btn_15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.btn_16.setText(QCoreApplication.translate("MainWindow", u"16", None))
    # retranslateUi

