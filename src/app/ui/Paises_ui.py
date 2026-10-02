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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_VentanaPaises(object):
    def setupUi(self, VentanaPaises):
        if not VentanaPaises.objectName():
            VentanaPaises.setObjectName(u"VentanaPaises")
        VentanaPaises.resize(563, 596)
        self.verticalLayout = QVBoxLayout(VentanaPaises)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(VentanaPaises)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineIDPais = QLineEdit(VentanaPaises)
        self.lineIDPais.setObjectName(u"lineIDPais")

        self.verticalLayout.addWidget(self.lineIDPais)

        self.label_2 = QLabel(VentanaPaises)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineNombrePais = QLineEdit(VentanaPaises)
        self.lineNombrePais.setObjectName(u"lineNombrePais")

        self.verticalLayout.addWidget(self.lineNombrePais)

        self.VistaPaises = QTableWidget(VentanaPaises)
        self.VistaPaises.setObjectName(u"VistaPaises")
        self.VistaPaises.setSupportedDragActions(Qt.DropAction.IgnoreAction)

        self.verticalLayout.addWidget(self.VistaPaises)

        self.stackedCRUDPais = QStackedWidget(VentanaPaises)
        self.stackedCRUDPais.setObjectName(u"stackedCRUDPais")
        self.PagBuscar = QWidget()
        self.PagBuscar.setObjectName(u"PagBuscar")
        self.horizontalLayout = QHBoxLayout(self.PagBuscar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pBuscarPais = QPushButton(self.PagBuscar)
        self.pBuscarPais.setObjectName(u"pBuscarPais")

        self.horizontalLayout.addWidget(self.pBuscarPais)

        self.stackedCRUDPais.addWidget(self.PagBuscar)
        self.PagInsertar = QWidget()
        self.PagInsertar.setObjectName(u"PagInsertar")
        self.horizontalLayout_3 = QHBoxLayout(self.PagInsertar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pInsertarPais = QPushButton(self.PagInsertar)
        self.pInsertarPais.setObjectName(u"pInsertarPais")

        self.horizontalLayout_3.addWidget(self.pInsertarPais)

        self.stackedCRUDPais.addWidget(self.PagInsertar)
        self.PagActualizar = QWidget()
        self.PagActualizar.setObjectName(u"PagActualizar")
        self.horizontalLayout_2 = QHBoxLayout(self.PagActualizar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pActualizarPais = QPushButton(self.PagActualizar)
        self.pActualizarPais.setObjectName(u"pActualizarPais")

        self.horizontalLayout_2.addWidget(self.pActualizarPais)

        self.stackedCRUDPais.addWidget(self.PagActualizar)
        self.PagEliminar = QWidget()
        self.PagEliminar.setObjectName(u"PagEliminar")
        self.horizontalLayout_4 = QHBoxLayout(self.PagEliminar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pEliminarPais = QPushButton(self.PagEliminar)
        self.pEliminarPais.setObjectName(u"pEliminarPais")

        self.horizontalLayout_4.addWidget(self.pEliminarPais)

        self.stackedCRUDPais.addWidget(self.PagEliminar)

        self.verticalLayout.addWidget(self.stackedCRUDPais, 0, Qt.AlignmentFlag.AlignBottom)


        self.retranslateUi(VentanaPaises)

        self.stackedCRUDPais.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(VentanaPaises)
    # setupUi

    def retranslateUi(self, VentanaPaises):
        VentanaPaises.setWindowTitle(QCoreApplication.translate("VentanaPaises", u"Paises", None))
        self.label.setText(QCoreApplication.translate("VentanaPaises", u"ID del pais", None))
        self.lineIDPais.setPlaceholderText(QCoreApplication.translate("VentanaPaises", u"Inserte el ID del pais", None))
        self.label_2.setText(QCoreApplication.translate("VentanaPaises", u"Nombre", None))
        self.lineNombrePais.setPlaceholderText(QCoreApplication.translate("VentanaPaises", u"Inserte el nombre del pais", None))
        self.pBuscarPais.setText(QCoreApplication.translate("VentanaPaises", u"Buscar", None))
        self.pInsertarPais.setText(QCoreApplication.translate("VentanaPaises", u"Insertar", None))
        self.pActualizarPais.setText(QCoreApplication.translate("VentanaPaises", u"Actualizar", None))
        self.pEliminarPais.setText(QCoreApplication.translate("VentanaPaises", u"Eliminar", None))
    # retranslateUi

