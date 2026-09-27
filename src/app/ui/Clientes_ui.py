# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Clientes.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1228, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(10, 110, 201, 41))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(740, 70, 221, 30))
        font = QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(500, 110, 211, 41))
        self.dateEdit.setCalendarPopup(True)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(240, 110, 201, 41))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(500, 70, 201, 30))
        self.label_4.setFont(font)
        self.dateEdit_2 = QDateEdit(self.centralwidget)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(740, 110, 211, 41))
        self.dateEdit_2.setCalendarPopup(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 70, 191, 30))
        self.label_3.setFont(font)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 220, 1261, 401))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 231, 30))
        self.label_7.setFont(font)
        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 50, 1221, 41))
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 100, 91, 25))
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(1010, 110, 150, 41))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1020, 70, 121, 30))
        self.label_6.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 170, 84, 25))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 241, 41))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setScaledContents(False)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 181, 30))
        self.label_2.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.comboBox_3.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fecha de Regreso", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Fecha de Salida", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ciudad Destino", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Viajes Disponibles", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Pasajeros", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Buscador de Viajes", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ciudad Origen", None))
    # retranslateUi

