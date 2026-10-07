# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Paises.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Paises(object):
    def setupUi(self, Paises):
        if not Paises.objectName():
            Paises.setObjectName(u"Paises")
        Paises.resize(413, 371)
        self.centralwidget = QWidget(Paises)
        self.centralwidget.setObjectName(u"centralwidget")
        self.TPaises = QTableWidget(self.centralwidget)
        self.TPaises.setObjectName(u"TPaises")
        self.TPaises.setGeometry(QRect(20, 110, 256, 192))
        self.BModificar = QPushButton(self.centralwidget)
        self.BModificar.setObjectName(u"BModificar")
        self.BModificar.setGeometry(QRect(310, 150, 81, 26))
        self.BGuardar = QPushButton(self.centralwidget)
        self.BGuardar.setObjectName(u"BGuardar")
        self.BGuardar.setGeometry(QRect(310, 110, 81, 26))
        self.BEliminar = QPushButton(self.centralwidget)
        self.BEliminar.setObjectName(u"BEliminar")
        self.BEliminar.setGeometry(QRect(310, 190, 81, 26))
        self.BSalir = QPushButton(self.centralwidget)
        self.BSalir.setObjectName(u"BSalir")
        self.BSalir.setGeometry(QRect(310, 270, 81, 26))
        self.EIdPais = QLineEdit(self.centralwidget)
        self.EIdPais.setObjectName(u"EIdPais")
        self.EIdPais.setGeometry(QRect(130, 30, 141, 26))
        self.ENombre = QLineEdit(self.centralwidget)
        self.ENombre.setObjectName(u"ENombre")
        self.ENombre.setGeometry(QRect(130, 70, 141, 26))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 40, 49, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 81, 20))
        Paises.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Paises)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 413, 33))
        Paises.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Paises)
        self.statusbar.setObjectName(u"statusbar")
        Paises.setStatusBar(self.statusbar)

        self.retranslateUi(Paises)

        QMetaObject.connectSlotsByName(Paises)
    # setupUi

    def retranslateUi(self, Paises):
        Paises.setWindowTitle(QCoreApplication.translate("Paises", u"MainWindow", None))
        self.BModificar.setText(QCoreApplication.translate("Paises", u"Modificar", None))
        self.BGuardar.setText(QCoreApplication.translate("Paises", u"Guardar", None))
        self.BEliminar.setText(QCoreApplication.translate("Paises", u"Eliminar", None))
        self.BSalir.setText(QCoreApplication.translate("Paises", u"Salir", None))
        self.label.setText(QCoreApplication.translate("Paises", u"ID PAIS", None))
        self.label_2.setText(QCoreApplication.translate("Paises", u"NOMBRE PAIS", None))
    # retranslateUi

