# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 410)
        MainWindow.setMinimumSize(QSize(300, 410))
        MainWindow.setMaximumSize(QSize(300, 410))
        MainWindow.setContextMenuPolicy(Qt.CustomContextMenu)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 10, 118, 351))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_ReturnToWorkshop = QPushButton(self.layoutWidget)
        self.btn_ReturnToWorkshop.setObjectName(u"btn_ReturnToWorkshop")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(20)
        font.setBold(True)
        self.btn_ReturnToWorkshop.setFont(font)
        self.btn_ReturnToWorkshop.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.btn_ReturnToWorkshop)

        self.btn_OutsourcedRtWh = QPushButton(self.layoutWidget)
        self.btn_OutsourcedRtWh.setObjectName(u"btn_OutsourcedRtWh")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.btn_OutsourcedRtWh.setFont(font1)

        self.verticalLayout.addWidget(self.btn_OutsourcedRtWh)

        self.btn_OriRepl = QPushButton(self.layoutWidget)
        self.btn_OriRepl.setObjectName(u"btn_OriRepl")
        self.btn_OriRepl.setFont(font1)

        self.verticalLayout.addWidget(self.btn_OriRepl)

        self.btn_Review = QPushButton(self.layoutWidget)
        self.btn_Review.setObjectName(u"btn_Review")
        self.btn_Review.setFont(font1)

        self.verticalLayout.addWidget(self.btn_Review)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4fdd\u7a0e\u597d\u4ef6", None))
        self.btn_ReturnToWorkshop.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u95f4\u8fd4\u4ed3", None))
        self.btn_OutsourcedRtWh.setText(QCoreApplication.translate("MainWindow", u"\u59d4\u5916\u8fd4\u4ed3", None))
        self.btn_OriRepl.setText(QCoreApplication.translate("MainWindow", u"\u539f\u4ef6\u66f4\u6362", None))
        self.btn_Review.setText(QCoreApplication.translate("MainWindow", u"\u590d\u6838", None))
    # retranslateUi

