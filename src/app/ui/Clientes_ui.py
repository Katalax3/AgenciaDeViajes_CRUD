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

class Ui_PCliente(object):
    def setupUi(self, PCliente):
        if not PCliente.objectName():
            PCliente.setObjectName(u"PCliente")
        PCliente.resize(1280, 720)
        self.centralwidget = QWidget(PCliente)
        self.centralwidget.setObjectName(u"centralwidget")
        self.CCiudadO = QComboBox(self.centralwidget)
        self.CCiudadO.setObjectName(u"CCiudadO")
        self.CCiudadO.setGeometry(QRect(10, 110, 201, 41))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(740, 70, 221, 30))
        font = QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.DFechaS = QDateEdit(self.centralwidget)
        self.DFechaS.setObjectName(u"DFechaS")
        self.DFechaS.setGeometry(QRect(500, 110, 211, 41))
        self.DFechaS.setCalendarPopup(True)
        self.CCiudadD = QComboBox(self.centralwidget)
        self.CCiudadD.setObjectName(u"CCiudadD")
        self.CCiudadD.setGeometry(QRect(240, 110, 201, 41))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(500, 70, 201, 30))
        self.label_4.setFont(font)
        self.DFechaR = QDateEdit(self.centralwidget)
        self.DFechaR.setObjectName(u"DFechaR")
        self.DFechaR.setGeometry(QRect(740, 110, 211, 41))
        self.DFechaR.setCalendarPopup(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 70, 191, 30))
        self.label_3.setFont(font)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 220, 1271, 401))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 231, 30))
        self.label_7.setFont(font)
        self.CViajesD = QComboBox(self.frame)
        self.CViajesD.setObjectName(u"CViajesD")
        self.CViajesD.setGeometry(QRect(10, 50, 1261, 41))
        self.BSeleccionar = QPushButton(self.frame)
        self.BSeleccionar.setObjectName(u"BSeleccionar")
        self.BSeleccionar.setGeometry(QRect(10, 100, 91, 25))
        self.SPasajeros = QSpinBox(self.centralwidget)
        self.SPasajeros.setObjectName(u"SPasajeros")
        self.SPasajeros.setGeometry(QRect(1010, 110, 150, 41))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1020, 70, 121, 30))
        self.label_6.setFont(font)
        self.BBuscar = QPushButton(self.centralwidget)
        self.BBuscar.setObjectName(u"BBuscar")
        self.BBuscar.setGeometry(QRect(10, 170, 84, 25))
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
        PCliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(PCliente)

        QMetaObject.connectSlotsByName(PCliente)
    # setupUi

    def retranslateUi(self, PCliente):
        PCliente.setWindowTitle(QCoreApplication.translate("PCliente", u"Agencia de Viaje - Panel de Clientes", None))
        self.CCiudadO.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("PCliente", u"Fecha de Regreso", None))
        self.label_4.setText(QCoreApplication.translate("PCliente", u"Fecha de Salida", None))
        self.label_3.setText(QCoreApplication.translate("PCliente", u"Ciudad Destino", None))
        self.label_7.setText(QCoreApplication.translate("PCliente", u"Viajes Disponibles", None))
        self.BSeleccionar.setText(QCoreApplication.translate("PCliente", u"Seleccionar", None))
        self.label_6.setText(QCoreApplication.translate("PCliente", u"Pasajeros", None))
        self.BBuscar.setText(QCoreApplication.translate("PCliente", u"Buscar", None))
        self.label.setText(QCoreApplication.translate("PCliente", u"Buscador de Viajes", None))
        self.label_2.setText(QCoreApplication.translate("PCliente", u"Ciudad Origen", None))
    # retranslateUi

