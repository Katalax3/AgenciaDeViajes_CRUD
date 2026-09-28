# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Empleados.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_PEmpleado(object):
    def setupUi(self, PEmpleado):
        if not PEmpleado.objectName():
            PEmpleado.setObjectName(u"PEmpleado")
        PEmpleado.resize(931, 600)
        self.centralwidget = QWidget(PEmpleado)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.BInicio = QPushButton(self.frame)
        self.BInicio.setObjectName(u"BInicio")

        self.verticalLayout.addWidget(self.BInicio)

        self.BViajes = QPushButton(self.frame)
        self.BViajes.setObjectName(u"BViajes")

        self.verticalLayout.addWidget(self.BViajes)

        self.BTrayectos = QPushButton(self.frame)
        self.BTrayectos.setObjectName(u"BTrayectos")

        self.verticalLayout.addWidget(self.BTrayectos)

        self.BClientes = QPushButton(self.frame)
        self.BClientes.setObjectName(u"BClientes")

        self.verticalLayout.addWidget(self.BClientes)

        self.BReservasBoletos = QPushButton(self.frame)
        self.BReservasBoletos.setObjectName(u"BReservasBoletos")

        self.verticalLayout.addWidget(self.BReservasBoletos)

        self.BPagos = QPushButton(self.frame)
        self.BPagos.setObjectName(u"BPagos")

        self.verticalLayout.addWidget(self.BPagos)

        self.BTransportes = QPushButton(self.frame)
        self.BTransportes.setObjectName(u"BTransportes")

        self.verticalLayout.addWidget(self.BTransportes)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.BSalir = QPushButton(self.frame)
        self.BSalir.setObjectName(u"BSalir")

        self.verticalLayout.addWidget(self.BSalir)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_Inicio = QWidget()
        self.page_Inicio.setObjectName(u"page_Inicio")
        self.verticalLayout_3 = QVBoxLayout(self.page_Inicio)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 244, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(self.page_Inicio)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(24)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_3 = QLabel(self.page_Inicio)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 243, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.page_Inicio)
        self.page_Viajes = QWidget()
        self.page_Viajes.setObjectName(u"page_Viajes")
        self.verticalLayout_2 = QVBoxLayout(self.page_Viajes)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.page_Viajes)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setPointSize(18)
        self.label_5.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_5)

        self.pushButton_14 = QPushButton(self.page_Viajes)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(50, 0))

        self.verticalLayout_2.addWidget(self.pushButton_14, 0, Qt.AlignmentFlag.AlignRight)

        self.tableView = QTableView(self.page_Viajes)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.stackedWidget.addWidget(self.page_Viajes)
        self.page_Trayectos = QWidget()
        self.page_Trayectos.setObjectName(u"page_Trayectos")
        self.verticalLayout_4 = QVBoxLayout(self.page_Trayectos)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.page_Trayectos)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_6)

        self.pushButton_13 = QPushButton(self.page_Trayectos)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(50, 0))

        self.verticalLayout_4.addWidget(self.pushButton_13, 0, Qt.AlignmentFlag.AlignRight)

        self.tableView_2 = QTableView(self.page_Trayectos)
        self.tableView_2.setObjectName(u"tableView_2")

        self.verticalLayout_4.addWidget(self.tableView_2)

        self.verticalSpacer_6 = QSpacerItem(20, 239, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.stackedWidget.addWidget(self.page_Trayectos)
        self.page_Clientes = QWidget()
        self.page_Clientes.setObjectName(u"page_Clientes")
        self.verticalLayout_5 = QVBoxLayout(self.page_Clientes)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.page_Clientes)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_7)

        self.BNuevo = QPushButton(self.page_Clientes)
        self.BNuevo.setObjectName(u"BNuevo")
        self.BNuevo.setMinimumSize(QSize(50, 0))

        self.verticalLayout_5.addWidget(self.BNuevo, 0, Qt.AlignmentFlag.AlignRight)

        self.tableView_3 = QTableView(self.page_Clientes)
        self.tableView_3.setObjectName(u"tableView_3")

        self.verticalLayout_5.addWidget(self.tableView_3)

        self.verticalSpacer_7 = QSpacerItem(20, 239, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)

        self.stackedWidget.addWidget(self.page_Clientes)
        self.page_Reservas_Boletos = QWidget()
        self.page_Reservas_Boletos.setObjectName(u"page_Reservas_Boletos")
        self.verticalLayout_6 = QVBoxLayout(self.page_Reservas_Boletos)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.page_Reservas_Boletos)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_8)

        self.pushButton_11 = QPushButton(self.page_Reservas_Boletos)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(50, 0))

        self.verticalLayout_6.addWidget(self.pushButton_11, 0, Qt.AlignmentFlag.AlignRight)

        self.tableView_4 = QTableView(self.page_Reservas_Boletos)
        self.tableView_4.setObjectName(u"tableView_4")

        self.verticalLayout_6.addWidget(self.tableView_4)

        self.verticalSpacer_8 = QSpacerItem(20, 239, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_8)

        self.stackedWidget.addWidget(self.page_Reservas_Boletos)
        self.page_Pagos = QWidget()
        self.page_Pagos.setObjectName(u"page_Pagos")
        self.verticalLayout_7 = QVBoxLayout(self.page_Pagos)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.page_Pagos)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.verticalLayout_7.addWidget(self.label_9)

        self.pushButton_10 = QPushButton(self.page_Pagos)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(85, 0))

        self.verticalLayout_7.addWidget(self.pushButton_10, 0, Qt.AlignmentFlag.AlignRight)

        self.tableView_5 = QTableView(self.page_Pagos)
        self.tableView_5.setObjectName(u"tableView_5")
        self.tableView_5.setMaximumSize(QSize(717, 220))

        self.verticalLayout_7.addWidget(self.tableView_5)

        self.verticalSpacer_9 = QSpacerItem(20, 261, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.stackedWidget.addWidget(self.page_Pagos)
        self.page_Transportes = QWidget()
        self.page_Transportes.setObjectName(u"page_Transportes")
        self.verticalLayout_8 = QVBoxLayout(self.page_Transportes)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_10 = QLabel(self.page_Transportes)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.verticalLayout_8.addWidget(self.label_10)

        self.pushButton_9 = QPushButton(self.page_Transportes)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(50, 0))

        self.verticalLayout_8.addWidget(self.pushButton_9, 0, Qt.AlignmentFlag.AlignRight)

        self.tableView_6 = QTableView(self.page_Transportes)
        self.tableView_6.setObjectName(u"tableView_6")

        self.verticalLayout_8.addWidget(self.tableView_6)

        self.verticalSpacer_10 = QSpacerItem(20, 239, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_10)

        self.stackedWidget.addWidget(self.page_Transportes)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        PEmpleado.setCentralWidget(self.centralwidget)

        self.retranslateUi(PEmpleado)

        self.BSalir.setDefault(False)
        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(PEmpleado)
    # setupUi

    def retranslateUi(self, PEmpleado):
        PEmpleado.setWindowTitle(QCoreApplication.translate("PEmpleado", u"Agencia de Viaje - Panel Empleado", None))
        self.label.setText(QCoreApplication.translate("PEmpleado", u"Agencia de Viaje", None))
        self.label_2.setText("")
        self.BInicio.setText(QCoreApplication.translate("PEmpleado", u"Inicio", None))
        self.BViajes.setText(QCoreApplication.translate("PEmpleado", u"Viajes", None))
        self.BTrayectos.setText(QCoreApplication.translate("PEmpleado", u"Trayectos", None))
        self.BClientes.setText(QCoreApplication.translate("PEmpleado", u"Clientes", None))
        self.BReservasBoletos.setText(QCoreApplication.translate("PEmpleado", u"Reservas y Boletos", None))
        self.BPagos.setText(QCoreApplication.translate("PEmpleado", u"Pagos", None))
        self.BTransportes.setText(QCoreApplication.translate("PEmpleado", u"Transportes", None))
        self.BSalir.setText(QCoreApplication.translate("PEmpleado", u"Salir", None))
        self.label_4.setText(QCoreApplication.translate("PEmpleado", u"Hola Empleado", None))
        self.label_3.setText(QCoreApplication.translate("PEmpleado", u"Tu proximo viaje comienza aqu\u00ed", None))
        self.label_5.setText(QCoreApplication.translate("PEmpleado", u" Viajes", None))
        self.pushButton_14.setText(QCoreApplication.translate("PEmpleado", u"+ Nuevo", None))
        self.label_6.setText(QCoreApplication.translate("PEmpleado", u"Trayectos", None))
        self.pushButton_13.setText(QCoreApplication.translate("PEmpleado", u"+ Nuevo", None))
        self.label_7.setText(QCoreApplication.translate("PEmpleado", u"Clientes", None))
        self.BNuevo.setText(QCoreApplication.translate("PEmpleado", u"+ Nuevo", None))
        self.label_8.setText(QCoreApplication.translate("PEmpleado", u"Reservas y Boletos", None))
        self.pushButton_11.setText(QCoreApplication.translate("PEmpleado", u"+ Nuevo", None))
        self.label_9.setText(QCoreApplication.translate("PEmpleado", u"Pagos", None))
        self.pushButton_10.setText(QCoreApplication.translate("PEmpleado", u"+ Nuevo", None))
        self.label_10.setText(QCoreApplication.translate("PEmpleado", u"Transportes", None))
        self.pushButton_9.setText(QCoreApplication.translate("PEmpleado", u"+ Nuevo", None))
    # retranslateUi

