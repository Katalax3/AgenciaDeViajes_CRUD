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

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(400, 579)
        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 100, 91, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Ingresar = QPushButton(Login)
        self.Ingresar.setObjectName(u"Ingresar")
        self.Ingresar.setGeometry(QRect(40, 390, 320, 48))
        self.Ingresar.setFont(font)
        self.EUsuarioCorreo = QLineEdit(Login)
        self.EUsuarioCorreo.setObjectName(u"EUsuarioCorreo")
        self.EUsuarioCorreo.setGeometry(QRect(40, 220, 320, 48))
        self.EUsuarioCorreo.setFont(font)
        self.EUsuarioCorreo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.BEmpleado = QPushButton(Login)
        self.buttonGroup = QButtonGroup(Login)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.BEmpleado)
        self.BEmpleado.setObjectName(u"BEmpleado")
        self.BEmpleado.setGeometry(QRect(210, 150, 87, 36))
        self.BEmpleado.setFont(font)
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 311, 41))
        font1 = QFont()
        font1.setPointSize(28)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.BCliente = QPushButton(Login)
        self.buttonGroup.addButton(self.BCliente)
        self.BCliente.setObjectName(u"BCliente")
        self.BCliente.setGeometry(QRect(110, 150, 87, 36))
        self.BCliente.setFont(font)
        self.EContrasena = QLineEdit(Login)
        self.EContrasena.setObjectName(u"EContrasena")
        self.EContrasena.setGeometry(QRect(40, 290, 320, 48))
        self.EContrasena.setFont(font)
        self.EContrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Bienvenido", None))
        self.Ingresar.setText(QCoreApplication.translate("Login", u"INGRESAR", None))
        self.EUsuarioCorreo.setPlaceholderText(QCoreApplication.translate("Login", u"Usuario o Correo Electronico", None))
        self.BEmpleado.setText(QCoreApplication.translate("Login", u"Empleado", None))
        self.label.setText(QCoreApplication.translate("Login", u"Agencia de Viajes", None))
        self.BCliente.setText(QCoreApplication.translate("Login", u"Cliente", None))
        self.EContrasena.setText("")
        self.EContrasena.setPlaceholderText(QCoreApplication.translate("Login", u"Contrase\u00f1a", None))
    # retranslateUi

