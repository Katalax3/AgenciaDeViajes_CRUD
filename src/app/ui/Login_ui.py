# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 580)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 100, 91, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(40, 390, 320, 48))
        self.pushButton_3.setFont(font)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 220, 320, 48))
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_2 = QPushButton(Dialog)
        self.buttonGroup = QButtonGroup(Dialog)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.pushButton_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 150, 87, 36))
        self.pushButton_2.setFont(font)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 311, 41))
        font1 = QFont()
        font1.setPointSize(28)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(Dialog)
        self.buttonGroup.addButton(self.pushButton)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 150, 87, 36))
        self.pushButton.setFont(font)
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(40, 290, 320, 48))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Bienvenido", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"INGRESAR", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Usuario o Correo Electronico", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Empleado", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Agencia de Viajes", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Cliente", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a", None))
    # retranslateUi

