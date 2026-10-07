# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Bancos.ui'
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

class Ui_VentanaBancos(object):
    def setupUi(self, VentanaBancos):
        if not VentanaBancos.objectName():
            VentanaBancos.setObjectName(u"VentanaBancos")
        VentanaBancos.resize(600, 450)
        self.verticalLayout = QVBoxLayout(VentanaBancos)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitulo = QLabel(VentanaBancos)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitulo)

        self.layoutCampos = QHBoxLayout()
        self.layoutCampos.setObjectName(u"layoutCampos")
        self.labelID = QLabel(VentanaBancos)
        self.labelID.setObjectName(u"labelID")

        self.layoutCampos.addWidget(self.labelID)

        self.lineIDBanco = QLineEdit(VentanaBancos)
        self.lineIDBanco.setObjectName(u"lineIDBanco")

        self.layoutCampos.addWidget(self.lineIDBanco)

        self.labelNombre = QLabel(VentanaBancos)
        self.labelNombre.setObjectName(u"labelNombre")

        self.layoutCampos.addWidget(self.labelNombre)

        self.lineNombreBanco = QLineEdit(VentanaBancos)
        self.lineNombreBanco.setObjectName(u"lineNombreBanco")

        self.layoutCampos.addWidget(self.lineNombreBanco)


        self.verticalLayout.addLayout(self.layoutCampos)

        self.stackedCRUDBanco = QStackedWidget(VentanaBancos)
        self.stackedCRUDBanco.setObjectName(u"stackedCRUDBanco")
        self.pageBuscar = QWidget()
        self.pageBuscar.setObjectName(u"pageBuscar")
        self.horizontalLayout_1 = QHBoxLayout(self.pageBuscar)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.pBuscarBanco = QPushButton(self.pageBuscar)
        self.pBuscarBanco.setObjectName(u"pBuscarBanco")

        self.horizontalLayout_1.addWidget(self.pBuscarBanco)

        self.stackedCRUDBanco.addWidget(self.pageBuscar)
        self.pageInsertar = QWidget()
        self.pageInsertar.setObjectName(u"pageInsertar")
        self.horizontalLayout_2 = QHBoxLayout(self.pageInsertar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pInsertarBanco = QPushButton(self.pageInsertar)
        self.pInsertarBanco.setObjectName(u"pInsertarBanco")

        self.horizontalLayout_2.addWidget(self.pInsertarBanco)

        self.stackedCRUDBanco.addWidget(self.pageInsertar)
        self.pageActualizar = QWidget()
        self.pageActualizar.setObjectName(u"pageActualizar")
        self.horizontalLayout_3 = QHBoxLayout(self.pageActualizar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pActualizarBanco = QPushButton(self.pageActualizar)
        self.pActualizarBanco.setObjectName(u"pActualizarBanco")

        self.horizontalLayout_3.addWidget(self.pActualizarBanco)

        self.stackedCRUDBanco.addWidget(self.pageActualizar)
        self.pageEliminar = QWidget()
        self.pageEliminar.setObjectName(u"pageEliminar")
        self.horizontalLayout_4 = QHBoxLayout(self.pageEliminar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pEliminarBanco = QPushButton(self.pageEliminar)
        self.pEliminarBanco.setObjectName(u"pEliminarBanco")

        self.horizontalLayout_4.addWidget(self.pEliminarBanco)

        self.stackedCRUDBanco.addWidget(self.pageEliminar)

        self.verticalLayout.addWidget(self.stackedCRUDBanco)

        self.VistaBancos = QTableWidget(VentanaBancos)
        self.VistaBancos.setObjectName(u"VistaBancos")

        self.verticalLayout.addWidget(self.VistaBancos)


        self.retranslateUi(VentanaBancos)

        self.stackedCRUDBanco.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(VentanaBancos)
    # setupUi

    def retranslateUi(self, VentanaBancos):
        VentanaBancos.setWindowTitle(QCoreApplication.translate("VentanaBancos", u"Gesti\u00f3n de Bancos", None))
        self.labelTitulo.setText(QCoreApplication.translate("VentanaBancos", u"Administraci\u00f3n de Bancos", None))
        self.labelID.setText(QCoreApplication.translate("VentanaBancos", u"ID Banco:", None))
        self.labelNombre.setText(QCoreApplication.translate("VentanaBancos", u"Nombre Banco:", None))
        self.pBuscarBanco.setText(QCoreApplication.translate("VentanaBancos", u"Buscar Banco", None))
        self.pInsertarBanco.setText(QCoreApplication.translate("VentanaBancos", u"Guardar Banco", None))
        self.pActualizarBanco.setText(QCoreApplication.translate("VentanaBancos", u"Actualizar Banco", None))
        self.pEliminarBanco.setText(QCoreApplication.translate("VentanaBancos", u"Eliminar Banco", None))
    # retranslateUi

