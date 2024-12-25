# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1037, 726)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 1021, 651))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.disable_avp_button = QPushButton(self.frame)
        self.disable_avp_button.setObjectName(u"disable_avp_button")
        self.disable_avp_button.setGeometry(QRect(730, 40, 75, 31))
        self.enable_avp_button = QPushButton(self.frame)
        self.enable_avp_button.setObjectName(u"enable_avp_button")
        self.enable_avp_button.setGeometry(QRect(650, 40, 75, 31))
        self.avp_status = QTextEdit(self.frame)
        self.avp_status.setObjectName(u"avp_status")
        self.avp_status.setGeometry(QRect(810, 40, 151, 30))
        self.avp_status.setMaximumSize(QSize(16777215, 30))
        self.set_frequency_button = QPushButton(self.frame)
        self.set_frequency_button.setObjectName(u"set_frequency_button")
        self.set_frequency_button.setGeometry(QRect(280, 150, 211, 31))
        self.set_frequency = QTextEdit(self.frame)
        self.set_frequency.setObjectName(u"set_frequency")
        self.set_frequency.setGeometry(QRect(30, 150, 231, 30))
        self.set_frequency.setMaximumSize(QSize(500, 30))
        self.get_name_button = QPushButton(self.frame)
        self.get_name_button.setObjectName(u"get_name_button")
        self.get_name_button.setGeometry(QRect(60, 320, 351, 51))
        self.get_info_button = QPushButton(self.frame)
        self.get_info_button.setObjectName(u"get_info_button")
        self.get_info_button.setGeometry(QRect(600, 320, 351, 51))
        self.response_text = QTextEdit(self.frame)
        self.response_text.setObjectName(u"response_text")
        self.response_text.setGeometry(QRect(10, 400, 1001, 241))
        self.set_level_button = QPushButton(self.frame)
        self.set_level_button.setObjectName(u"set_level_button")
        self.set_level_button.setGeometry(QRect(280, 190, 211, 31))
        self.set_level = QTextEdit(self.frame)
        self.set_level.setObjectName(u"set_level")
        self.set_level.setGeometry(QRect(30, 190, 231, 30))
        self.set_level.setMaximumSize(QSize(500, 30))
        self.set_bias_button = QPushButton(self.frame)
        self.set_bias_button.setObjectName(u"set_bias_button")
        self.set_bias_button.setGeometry(QRect(280, 230, 211, 31))
        self.set_bias = QTextEdit(self.frame)
        self.set_bias.setObjectName(u"set_bias")
        self.set_bias.setGeometry(QRect(30, 230, 231, 30))
        self.set_bias.setMaximumSize(QSize(500, 30))
        self.connection_button = QPushButton(self.frame)
        self.connection_button.setObjectName(u"connection_button")
        self.connection_button.setGeometry(QRect(190, 40, 75, 31))
        self.combo_com_port = QComboBox(self.frame)
        self.combo_com_port.addItem("")
        self.combo_com_port.addItem("")
        self.combo_com_port.addItem("")
        self.combo_com_port.addItem("")
        self.combo_com_port.addItem("")
        self.combo_com_port.addItem("")
        self.combo_com_port.addItem("")
        self.combo_com_port.addItem("")
        self.combo_com_port.addItem("")
        self.combo_com_port.setObjectName(u"combo_com_port")
        self.combo_com_port.setGeometry(QRect(30, 40, 151, 31))
        self.mode_button = QPushButton(self.frame)
        self.mode_button.setObjectName(u"mode_button")
        self.mode_button.setGeometry(QRect(190, 80, 75, 31))
        self.combo_mode = QComboBox(self.frame)
        self.combo_mode.addItem("")
        self.combo_mode.addItem("")
        self.combo_mode.setObjectName(u"combo_mode")
        self.combo_mode.setGeometry(QRect(30, 80, 151, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1037, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.disable_avp_button.setText(QCoreApplication.translate("MainWindow", u"Disable AVP", None))
        self.enable_avp_button.setText(QCoreApplication.translate("MainWindow", u"Enable AVP", None))
        self.set_frequency_button.setText(QCoreApplication.translate("MainWindow", u"Set Frequency", None))
        self.get_name_button.setText(QCoreApplication.translate("MainWindow", u"Get Device Name", None))
        self.get_info_button.setText(QCoreApplication.translate("MainWindow", u"Get Full Info", None))
        self.set_level_button.setText(QCoreApplication.translate("MainWindow", u"Set Level", None))
        self.set_bias_button.setText(QCoreApplication.translate("MainWindow", u"Set Bias", None))
        self.connection_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.combo_com_port.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.combo_com_port.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.combo_com_port.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.combo_com_port.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.combo_com_port.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))
        self.combo_com_port.setItemText(5, QCoreApplication.translate("MainWindow", u"COM6", None))
        self.combo_com_port.setItemText(6, QCoreApplication.translate("MainWindow", u"COM7", None))
        self.combo_com_port.setItemText(7, QCoreApplication.translate("MainWindow", u"COM8", None))
        self.combo_com_port.setItemText(8, QCoreApplication.translate("MainWindow", u"COM9", None))

        self.mode_button.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.combo_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"R-X", None))
        self.combo_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"C-f", None))

    # retranslateUi

