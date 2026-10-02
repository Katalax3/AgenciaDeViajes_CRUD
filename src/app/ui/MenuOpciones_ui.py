# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuOpciones.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QWidget)

class Ui_MenuOpciones(object):
    def setupUi(self, MenuOpciones):
        if not MenuOpciones.objectName():
            MenuOpciones.setObjectName(u"MenuOpciones")
        MenuOpciones.resize(1280, 720)
        MenuOpciones.setAutoFillBackground(False)
        self.actionPaises = QAction(MenuOpciones)
        self.actionPaises.setObjectName(u"actionPaises")
        self.actionParcialidades = QAction(MenuOpciones)
        self.actionParcialidades.setObjectName(u"actionParcialidades")
        self.actionBancos = QAction(MenuOpciones)
        self.actionBancos.setObjectName(u"actionBancos")
        self.centralwidget = QWidget(MenuOpciones)
        self.centralwidget.setObjectName(u"centralwidget")
        MenuOpciones.setCentralWidget(self.centralwidget)
        self.menuBarMO = QMenuBar(MenuOpciones)
        self.menuBarMO.setObjectName(u"menuBarMO")
        self.menuBarMO.setGeometry(QRect(0, 0, 1280, 30))
        self.menuBarMO.setNativeMenuBar(True)
        self.menuTablas = QMenu(self.menuBarMO)
        self.menuTablas.setObjectName(u"menuTablas")
        self.menuTablas.setEnabled(True)
        self.menuTablas.setTearOffEnabled(False)
        self.menuTablas.setSeparatorsCollapsible(False)
        MenuOpciones.setMenuBar(self.menuBarMO)

        self.menuBarMO.addAction(self.menuTablas.menuAction())
        self.menuTablas.addAction(self.actionPaises)
        self.menuTablas.addAction(self.actionParcialidades)
        self.menuTablas.addAction(self.actionBancos)

        self.retranslateUi(MenuOpciones)

        QMetaObject.connectSlotsByName(MenuOpciones)
    # setupUi

    def retranslateUi(self, MenuOpciones):
        MenuOpciones.setWindowTitle(QCoreApplication.translate("MenuOpciones", u"Men\u00fa de Opciones", None))
        self.actionPaises.setText(QCoreApplication.translate("MenuOpciones", u"Paises", None))
        self.actionParcialidades.setText(QCoreApplication.translate("MenuOpciones", u"Parcialidades", None))
        self.actionBancos.setText(QCoreApplication.translate("MenuOpciones", u"Bancos", None))
        self.menuTablas.setTitle(QCoreApplication.translate("MenuOpciones", u"Tablas", None))
    # retranslateUi

