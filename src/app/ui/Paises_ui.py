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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableView,
    QWidget)

class Ui_VentanaPaises(object):
    def setupUi(self, VentanaPaises):
        if not VentanaPaises.objectName():
            VentanaPaises.setObjectName(u"VentanaPaises")
        VentanaPaises.resize(563, 593)
        VentanaPaises.setMaximumSize(QSize(563, 16777215))
        self.gridLayout = QGridLayout(VentanaPaises)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineIDPais = QLineEdit(VentanaPaises)
        self.lineIDPais.setObjectName(u"lineIDPais")

        self.gridLayout.addWidget(self.lineIDPais, 1, 0, 1, 2)

        self.label_2 = QLabel(VentanaPaises)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.ppaisBuscar = QPushButton(VentanaPaises)
        self.ppaisBuscar.setObjectName(u"ppaisBuscar")

        self.gridLayout.addWidget(self.ppaisBuscar, 7, 0, 1, 1)

        self.ppaisNuevo = QPushButton(VentanaPaises)
        self.ppaisNuevo.setObjectName(u"ppaisNuevo")

        self.gridLayout.addWidget(self.ppaisNuevo, 5, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.ppaisEliminar = QPushButton(VentanaPaises)
        self.ppaisEliminar.setObjectName(u"ppaisEliminar")

        self.gridLayout.addWidget(self.ppaisEliminar, 7, 1, 1, 1)

        self.lineNombrePais = QLineEdit(VentanaPaises)
        self.lineNombrePais.setObjectName(u"lineNombrePais")

        self.gridLayout.addWidget(self.lineNombrePais, 3, 0, 1, 2)

        self.ppaisActualizar = QPushButton(VentanaPaises)
        self.ppaisActualizar.setObjectName(u"ppaisActualizar")

        self.gridLayout.addWidget(self.ppaisActualizar, 5, 0, 1, 1)

        self.label = QLabel(VentanaPaises)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.vistaPaises = QTableView(VentanaPaises)
        self.vistaPaises.setObjectName(u"vistaPaises")

        self.gridLayout.addWidget(self.vistaPaises, 6, 0, 1, 2)


        self.retranslateUi(VentanaPaises)

        QMetaObject.connectSlotsByName(VentanaPaises)
    # setupUi

    def retranslateUi(self, VentanaPaises):
        VentanaPaises.setWindowTitle(QCoreApplication.translate("VentanaPaises", u"Paises", None))
        self.lineIDPais.setPlaceholderText(QCoreApplication.translate("VentanaPaises", u"Inserte el ID del pais", None))
        self.label_2.setText(QCoreApplication.translate("VentanaPaises", u"Nombre", None))
        self.ppaisBuscar.setText(QCoreApplication.translate("VentanaPaises", u"Buscar", None))
        self.ppaisNuevo.setText(QCoreApplication.translate("VentanaPaises", u"Nuevo+", None))
        self.ppaisEliminar.setText(QCoreApplication.translate("VentanaPaises", u"Eliminar", None))
        self.lineNombrePais.setPlaceholderText(QCoreApplication.translate("VentanaPaises", u"Inserte el nombre del pais", None))
        self.ppaisActualizar.setText(QCoreApplication.translate("VentanaPaises", u"Actualizar", None))
        self.label.setText(QCoreApplication.translate("VentanaPaises", u"ID del pais", None))
    # retranslateUi

